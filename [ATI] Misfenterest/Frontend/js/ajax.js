function doAjaxPage(type,username){ //busca 5 imagenes segun el tipo de busqueda ('all','upload','pin') y las retorna en un json
	var retorno;
	var pagineType;
	if(general){
		pagineType = page;
	}
	else{
		pagineType = pagePin;
	} 
	$.ajax({
		type: "GET",
		url: urlImages,
		data: {'page':pagineType,'type':type, 'username':username},
		async: false,
		success: function(data){
			retorno = JSON.parse(data);
			if(retorno != "vacio" && retorno.length>0){
				
				if(general){
					page = page+(retorno.length);
				}
				else{
					pagePin = pagePin+(retorno.length);
				}
			}
			else{
				retorno = false;
			}
		},
		error: function(xhr){
            //alert("An error occured: " + xhr.status + " " + xhr.statusText);
			retorno = "An error occured: " + xhr.status + " " + xhr.statusText;
			//mostrarError(retorno);
			alert(retorno);
			retorno = false;
		}
	});

	return retorno;

}

function doAjaxEditarPerfil(name,fullname,userAbout){
	var retorno;
	$.ajax({
		type: "GET",
		url: urlEditPerfil,
		data: {'name':name, 'fullname':fullname,'userAbout':userAbout},
		async: false,
		success: function(data){
			retorno = data;
			//alert("hola soy ajax "+retorno);
			if(retorno.length>0 && retorno == "exito"){
				
				retorno = true;
			}
			else{
				retorno = false;
			}
		},
		error: function(xhr){
            //alert("An error occured: " + xhr.status + " " + xhr.statusText);
			retorno = "An error occured: " + xhr.status + " " + xhr.statusText;
			//mostrarError(retorno);
			alert(retorno);
			retorno = false;
		}
	});

	return retorno;
}

function doAjaxPin(name,picdir,tipo){
	var retorno;
	$.ajax({
		type: "GET",
		url: urlPin,
		data: {'name':name, 'picdir':picdir,'tipo':tipo},
		async: false,
		success: function(data){
			retorno = data;
			//alert("hola soy ajax "+retorno);
			if(retorno.length>0 && retorno == "exito"){
				
				retorno = true;
			}
			else{
				retorno = false;
			}
		},
		error: function(xhr){
            //alert("An error occured: " + xhr.status + " " + xhr.statusText);
			retorno = "An error occured: " + xhr.status + " " + xhr.statusText;
			//mostrarError(retorno);
			alert(retorno);
			retorno = false;
		}
	});

	return retorno;	

}

