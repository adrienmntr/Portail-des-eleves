import * as express from "express";
import socketioJwt from 'socketio-jwt';
import socketIo from 'socket.io';
import { createServer, Server, request } from 'http';
import {add, get} from './db';

class Message {
	constructor(public user_id: string, public message: string, posted_on: Date){}
}

/**
 * The JWT authentication is made with https://github.com/auth0-community/auth0-socketio-jwt
 */

const app = express();
app.set("port", process.env.PORT || 3000);

let httpServer = createServer(app);
let io = socketIo(httpServer);

io
.on('connection', socketioJwt.authorize({
	secret: 'your secret or public key',
	handshake: true,
	decodedPropertyName: ""
}))
.on("authenticated", (socket: any) => {

	socket.on("message", (request: any) => {
		if (request.message === undefined ){
			return
		}

		let model = new Message(socket.decoded_token.username, request.message, new Date());
		add(model.user_id, model.message);
		socket.broadcast(model);
	});

	socket.on("fetch", (request: any) => {
		if (request.from === undefined || request.limit === undefined){
			return 
		}

		let messages = await get(request.from, request.limit);
		socket.emit("fetch_response", messages);
	});

});

const server = httpServer.listen(3000, () => {
  console.log("listening on *:3000");
});