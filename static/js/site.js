function sendRequest(param)
{
	//baseline url
	var url = "http://127.0.0.1:5000/";

	url = url+param;

		// function reqListener(){
	window.location.replace(url);
	// }

	// //put a request into FLASK
	// var oReq = new XMLHttpRequest();
 //    oReq.addEventListener("load", reqListener);
 //    oReq.open("GET", url);
 //    oReq.send();
}