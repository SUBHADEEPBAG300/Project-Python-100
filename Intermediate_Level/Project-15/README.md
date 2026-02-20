# 💬 Chat Application (Python + Sockets + Threading)

A simple **real-time chat application** built in Python using **Sockets, Networking, and Threading**.  
This project demonstrates how multiple clients can connect to a server and exchange messages simultaneously.

---

## 📖 Overview
This Chat Application allows multiple users to communicate with each other in real time.  
- The **server** manages connections and broadcasts messages.  
- Each **client** connects to the server, chooses a nickname, and can send/receive messages.  
- Uses **threading** to handle multiple clients concurrently.  

---

## 🚀 Features
- **Multi-client support**: Multiple users can join the chat at the same time.  
- **Nicknames**: Each client chooses a nickname when connecting.  
- **Broadcast messaging**: Messages are sent to all connected clients.  
- **Threading**: Ensures smooth communication without blocking.  
- **Error handling**: Detects disconnections and removes clients gracefully.  

---

## 🛠️ Requirements
- Python **3.8+**  
- No external libraries required (uses built-in `socket` and `threading` modules).  

---

## 📂 Project Structure
```
chat-app/
│
├── server.py   # Server-side code
├── client.py   # Client-side code
└── README.md   # Documentation
```

---

## ▶️ How to Run

1. **Start the server** (in one terminal):
   ```bash
   python server.py
   ```

2. **Start a client** (in another terminal):
   ```bash
   python client.py
   ```
   Enter a nickname when prompted.

3. **Start more clients** (open additional terminals and run `client.py`).  
   Each client can send and receive messages in real time.

---

## 🎮 Example Flow

**Terminal 1 (Server):**
```
Server is running and listening...
Connected with ('127.0.0.1', 54321)
Nickname of client is Jiban
```

**Terminal 2 (Client 1):**
```
Choose your nickname: Jiban
Connected to the server!
Jiban: Hello everyone!
```

**Terminal 3 (Client 2):**
```
Choose your nickname: Alice
Connected to the server!
Jiban: Hello everyone!
Alice: Hi Jiban!
```

---

## 🧠 How It Works
- **Server (`server.py`)**  
  - Listens for incoming connections.  
  - Stores connected clients and nicknames.  
  - Broadcasts messages to all clients.  

- **Client (`client.py`)**  
  - Connects to the server.  
  - Sends chosen nickname.  
  - Runs two threads:  
    - One for receiving messages.  
    - One for sending messages.  

---

## 💻 Supported Platforms
This project is cross-platform and works on:  
- **Windows** (tested on Windows 10/11)  
- **Linux** (Ubuntu, Fedora, etc.)  
- **macOS** (latest versions)  

⚠️ Note: Ensure Python is installed and added to PATH.  
For multiple clients, open separate terminals or command prompts.  

---

## 👨‍💻 Author
**Jiban**  
- 🎓 Student at Brainware University, Barasat, West Bengal, India  
- 🔗 GitHub: [github.com/Jiban0507](https://github.com/Jiban0507)  

---

## 📌 Future Improvements
- Add **private messaging** between clients.  
- Implement a **GUI interface** using Tkinter or PyQt.  
- Add **encryption** for secure communication.  
- Maintain a **chat history** log file.  

---

## 💡 Learning Outcomes
By studying this project, you will learn:
- How to use **Python sockets** for networking.  
- How to implement a **multi-threaded server**.  
- How to manage **real-time communication** between multiple clients.  
- How to structure a simple **network application**.  
