function generationUP() {
	var username = $("#nombreUsuario").text();
	var busqueda = "upload";
	var aux;
	var cont;
	if(!general){
		busqueda = "pin";
	}
	var objetos = doAjaxPage(busqueda,username); 
	if(objetos && objetos != undefined && objetos != "fallo"){
		//alert("HOlaaaaa");
		
		//alert(objetos.length);
		for(var i=0; i<objetos.length; i++){
			
			n = 150+Math.floor((Math.random() * 130) + 1);
			
			if(general){
				
				if(objetos[i]["isPin"]=="True"){
					isPin[cant] = true;
				}
				else{
					isPin[cant] = false;
				}
				aux = cant;
			}
			else{
				aux = cantPin;
			}
			
			cont = '<div class ="row sombraImagen" style = "background-color: white; margin-left:1px; margin-top:5%; border-radius: 4px;">';
			cont +=      '<a href="#" style ="border-radius: 4px" onclick = "mostrarImagen('+aux+');">';
			cont +=          '<img  width="100%" height="'+n+'px" src="'+ objetos[i]["picdir"] +'" class="img-rounded"/>'
			cont +=      '</a>'
			cont +=    '<div class="caption">'
			cont +=         '<h3>'+objetos[i]["title"]+'</h3>'
			cont +=          '<p>'+objetos[i]["description"]+'</p>'
			cont +=    '</div>'
			cont +='</div>';  
			if(general){
				$("#content"+j).append(cont);
				cant = cant + 1;
			}
			else{
				$("#pin"+j).append(cont);
				cantPin = cantPin + 1;
			}
			if(j==4){
				 j = 1;
			}
			else{
				j = j + 1;
			}
			
		}
		if(general){
			images = images.concat(objetos);
		}
		else{
			imagesPin = imagesPin.concat(objetos);
		}
		
	} 
 }
 

	
