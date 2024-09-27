import React, { useState, useRef } from 'react';

const AIChatbot = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const conversationHistory = useRef([]); // For storing conversation history
  const chatContainerRef = useRef(null); // To reference the chat container for scrolling

  // Page and chat container styles
  const pageStyle = {
    minHeight: '100vh',
    width: '99vw',
    backgroundColor: '#1c1c1c',
    color: '#fff',
    padding: '20px',
    boxSizing: 'border-box',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
  };

  const chatContainerStyle = {
    width: '100%',
    maxWidth: '1450px',
    backgroundColor: '#333',
    borderRadius: '10px',
    padding: '20px',
    boxSizing: 'border-box',
    boxShadow: '0px 4px 10px rgba(0, 0, 0, 0.2)',
    height: '75vh', // Set a fixed height
    overflowY: 'scroll', // Scrollable content
    marginTop:'-12vh',
    marginBottom: '-5vh'
  };

  const messageStyle = {
    backgroundColor: '#444',
    padding: '10px',
    borderRadius: '8px',
    margin: '10px 0',
    color: '#fff',
  };

  const inputContainerStyle = {
    display: 'flex',
    width: '100%',
    marginTop: '20px',
    maxWidth: '1400px',
  };

  const inputStyle = {
    flex: '1',
    padding: '10px',
    borderRadius: '5px',
    border: 'none',
    fontSize: '16px',
  };

  const buttonStyle = {
    backgroundColor: '#00bfa5',
    color: '#fff',
    padding: '10px 15px',
    border: 'none',
    borderRadius: '5px',
    cursor: 'pointer',
    fontSize: '16px',
    marginLeft: '10px',
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = { role: 'user', content: input };
    conversationHistory.current.push(userMessage);
    setMessages(prevMessages => [...prevMessages, { text: input, type: 'user' }]);
    setInput('');

    await fetchAPI();
  };

  const fetchAPI = async () => {
    const apiKey = meta.env.VITE_OPENAI_API_KEY;

    try {
      const response = await fetch('https://api.openai.com/v1/chat/completions', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${apiKey}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          model: 'gpt-4',
          messages: conversationHistory.current,
          stream: true,
        }),
      });

      const botMessage = { text: '', type: 'bot' };
      setMessages(prevMessages => [...prevMessages, botMessage]);

      const reader = response.body.getReader();
      const decoder = new TextDecoder('utf-8');
      let done = false;
      let result = '';

      while (!done) {
        const { done: streamDone, value } = await reader.read();
        done = streamDone;

        const chunk = decoder.decode(value, { stream: true });
        chunk.split('\n').forEach(line => {
          if (line.startsWith('data:')) {
            const jsonData = line.replace('data: ', '');
            if (jsonData === '[DONE]') {
              done = true;
            } else {
              try {
                const parsedData = JSON.parse(jsonData);
                const content = parsedData.choices[0].delta.content || '';
                result += content;
                setMessages(prevMessages => {
                  const updatedMessages = [...prevMessages];
                  updatedMessages[updatedMessages.length - 1].text = result; // Update last bot message
                  return updatedMessages;
                });
              } catch (e) {
                console.error('Error parsing JSON:', e);
              }
            }
          }
        });

        // Auto-scroll to bottom of chat
        if (chatContainerRef.current) {
          chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
        }
      }

      conversationHistory.current.push({ role: 'assistant', content: result });

    } catch (error) {
      console.error('Error:', error);
      setMessages(prevMessages => [
        ...prevMessages,
        { text: 'An error occurred.', type: 'bot' },
      ]);
    }
  };

  return (
    <div style={pageStyle}>
      <div style={chatContainerStyle} ref={chatContainerRef}>
        <h2>AI Chatbot</h2>
        <div>
          {messages.map((message, index) => (
            <div key={index} style={messageStyle}>
              <strong>{message.type === 'user' ? 'You' : 'AI'}:</strong> {message.text}
            </div>
          ))}
        </div>
      </div>
      <form onSubmit={handleSubmit} style={inputContainerStyle}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          style={inputStyle}
          placeholder="Type your message here..."
        />
        <button type="submit" style={buttonStyle}>
          Send
        </button>
      </form>
    </div>
  );
};

export default AIChatbot;
