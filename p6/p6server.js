// Name:        Ben Belden
// Class ID#:   bpb2v
// Section:     CSCI 6180-001
// Assignment:  Lab #6
// Due:         16:20:00, December 1, 2017
// Purpose: 	Build both the client and server sides of a web-based app that 
//				provides your p5 alignment program as a service. The client side 
//				should support drag-and-drop a file of a pair of strings onto a 
//				dropzone on a web page.
//				The client should use websockets to transfer the strings to node-
//				based server that runs your alignment program and sends the results 
//				back to be displayed by the client.
//				The server should be built using nodejs and should use websockets 
//				to receive a pair of strings to be aligned.  It should drive a new 
//				process that executes the alignment program, and feed the strings 
//				to it via its stdin, and should capture its stdout, and transfer 
//				the result to the client running in a browser.
// Input:       From preformatted file.  
// Outut:       To website.
// 
// File:        p6server.js


const WebSocket = require("ws");
const spawn = require("child_process").spawn

const websocket_server = new WebSocket.Server({port: 5907});
websocket_server.on("connection", function(websocket) {
	console.log("New websocket connection from %s:%d", websocket._socket.remoteAddress, websocket._socket.remotePort);
	websocket.on("message", function(incoming_message) {
		console.log("Received message \n%s\nof length %d from the client", incoming_message, incoming_message.length);
		rev = spawn("/usr/bin/python", ["p6fakealign.py"]);
		rev.stdout.on("data", function(data) {
			websocket.send(data);
		});
		rev.stdin.write(incoming_message);
		rev.stdin.end()
	});
});

