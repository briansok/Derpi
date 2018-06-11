/* Settings */

var wsUri = "wss://"+document.domain+"";
var output;

if (document.domain == '127.0.0.1') {
	var wsUri = "ws://"+document.domain+":8000/";
}

function init() {
	output = document.getElementById("output");
	setupSocket();
}

function setupSocket() {
	websocket = new WebSocket(wsUri);
	websocket.onopen = function(evt) { onOpen(evt) };
	websocket.onclose = function(evt) { onClose(evt) };
	websocket.onmessage = function(evt) { onMessage(evt) };
	websocket.onerror = function(evt) { onError(evt) };
}

// On open event
function onOpen(evt) {
	$('.node-status').removeClass('node-disconnected');
	$('.node-status').addClass('node-connected');
}

// On close event
function onClose(evt) {
	$('.node-status').removeClass('node-connected');
	$('.node-status').addClass('node-disconnected');
}

// On server resonse
function onMessage(evt) {
	var data = JSON.parse(evt.data);
	console.log(data);
	checkbox_class = '.uid-'+ data.id+' input';
	if (data.value == 1) {
		$(checkbox_class).prop('checked', true);	
	} else {
		$(checkbox_class).prop('checked', false);	
	}

	if (data.type == "OU") {
		var ou_el = $('label[data-token="' + data.token + '"]');
		ou_el.html(data.value);
	}
}

// Displays an error
function onError(evt) {
	writeToScreen('<span style="color: red;">ERROR:</span> ' + evt.data);
}

// On server resonse
function doSend(message) {
	writeToScreen("SENT: " + message);
	websocket.send(message);
}

// @todo this function was for debugging this could be used for error reporting to the front-end
function writeToScreen(message) {
	var pre = document.createElement("p");
	pre.style.wordWrap = "break-word";
	pre.innerHTML = message;
	output.appendChild(pre);
}

window.addEventListener("load", init, false);

// Switch for checkbox

$(".switch-check").on('click',function() {
	var sensor_state;
	sensor_id = $(this).attr('id');
	sensor_type = $(this).attr('data-type');
	sensor_gpio = $(this).attr('data-gpio');
	sensor_token = $(this).attr('data-token');
	sensor_read = 0;

	if($(this).is(":checked")) {
		sensor_state = 1;
	} else {
		sensor_state = 0;
	}

	console.log(sensor_state);

	websocket.send(JSON.stringify({
		id: sensor_id,
		value: sensor_state,
		token: sensor_token,
		type: sensor_type, 
		gpio: sensor_gpio,
		read: sensor_read 
	}));
});
