
function setText(text, arg){
	arg.getElementsByClassName("tmielementtext")[0].innerHTML=text;
}
function setDisplay(){
	if(document.getElementById("TMItot").style.display=="flex"){
		document.getElementById("TMItot").style.display="none";
		document.getElementById("img").src="/symbol/angledown.png";
		document.getElementById("TMItot").scrollIntoView();
	}else{
		document.getElementById("TMItot").style.display="flex";
		document.getElementById("img").src="/symbol/angleup.png";
		document.getElementById("chart").scrollIntoView();
	}
	
}
function addTMI(mint_temp,max_temp,precip,snow,wind,humid,sun,cloud) {
	var tmi = document.createElement('div');
	document.getElementById("TMI").appendChild(tmi);
	window.scrollBy(0,600);
}
