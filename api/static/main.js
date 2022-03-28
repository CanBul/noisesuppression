
const recorder = document.getElementById('recorder');
recorder.addEventListener('change', function(e) {
    const file = e.target.files[0];
	const url = URL.createObjectURL(file);
	var au = document.createElement('audio');
	var li = document.createElement('div');
	

	//add controls to the <audio> element
	au.controls = true;
	au.src = url;
    
    // Do something with the audio file.
    document.getElementById('noisy').style.display = "block"

	li.appendChild(au);
	const recordingsList = document.getElementById('recordingsList')
	

	if (recordingsList.childElementCount>=1) {
		
		recordingsList.firstElementChild.replaceWith(li);
	} else {
		recordingsList.appendChild(li);
	}
	
  });




const form = document.getElementById('form');

form.addEventListener('submit', onSubmit);

function onSubmit(e) {
	
    
    e.preventDefault();
	document.getElementById("loading").style.display ="flex";
	
	
    const file = document.getElementById('recorder').files[0];
	

	if ((typeof file === 'undefined') && (recordingsList.childElementCount<1)) {
		alert('Please upload a wav file')
		document.getElementById("loading").style.display ="none";
	}
	
	if (typeof file !== 'undefined') {
		var xhr=new XMLHttpRequest();
		

		xhr.onload=function(e) {
			
			if(this.readyState === 4) {
				console.log("Server returned: ",e.target.responseText);
				
				results = document.getElementById('result-section')
				
				while (results.firstChild) {
					results.firstChild.remove()
				}

				results.style.display = 'flex';
				results.style.flexDirection ="column";				
				results.style.justifyContent ="space-between";

				var el = document.createElement("p")
				el.innerText = "Noisy Spectrogram"
				results.appendChild(el)

				var img = document.createElement("img");
				img.src = "/static/spectrograms/noisy.png";
				results.appendChild(img)

				var el = document.createElement("p")
				el.innerText = "Cleaned Sound"
				results.appendChild(el)

				var au = document.createElement('audio');				
				au.controls = true;
				au.src = "/static/results/fromServer.wav";
				results.appendChild(au)

				var el = document.createElement("p")
				el.innerText = "Cleaned Spectrogram"
				results.appendChild(el)

				var img = document.createElement("img");
				img.src = "/static/spectrograms/clean.png";
				results.appendChild(img)


			
				document.getElementById("loading").style.display ="none";
				

				
				 
			}
		};
		var fd=new FormData();
		fd.append("audio_data",file, 'filee');
		xhr.open("POST","/process",true);
		xhr.send(fd);
		
	} 
	
    
}


