const socket = new WebSocket('ws://localhost:8000/ws');

const messages = document.getElementById('messages');
const form = document.getElementById('form');
const input = document.getElementById('message');
const username = document.getElementById('username');
const status = document.getElementById('status');
const sendButton = document.getElementById('send');

sendButton.disabled = true;

function getTime () {
  return new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

function addMessage (text, type, author) {
  const div = document.createElement('div');
  div.className = 'message ' + type;

  if (type !== 'info') {
    const meta = document.createElement('span');
    meta.className = 'meta';
    meta.textContent = author + ' · ' + getTime();
    div.appendChild(meta);
  }

  const body = document.createElement('span');
  body.textContent = text;
  div.appendChild(body);

  messages.appendChild(div);
  messages.scrollTop = messages.scrollHeight;
}

socket.onopen = () => {
  status.textContent = 'Connected';
  status.className = 'status online';
  sendButton.disabled = false;
  addMessage('Connected to the server', 'info');
};

socket.onmessage = (event) => {
  addMessage(event.data, 'received', 'Server');
};

socket.onclose = () => {
  status.textContent = 'Disconnected';
  status.className = 'status offline';
  sendButton.disabled = true;
  addMessage('Connection lost', 'info');
};

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const text = input.value;
  if (text.trim() === '' || socket.readyState !== WebSocket.OPEN) {
    return;
  }

  const name = username.value.trim() || 'Me';
  socket.send(text);
  addMessage(text, 'sent', name);
  input.value = '';
  input.focus();
});
