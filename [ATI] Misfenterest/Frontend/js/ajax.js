function doAjaxPage(type){ //busca 5 imagenes segun el tipo de busqueda ('all','upload','pin') y las retorna en un json
	var retorno;
	$.ajax({
		type: "GET",
		url: urlImages,
		data: {'page':page,'type':type},
		async: false,
		success: function(data){
			retorno = JSON.parse(data);
			//alert("hola soy ajax "+retorno);
			if(retorno != "vacio" && retorno.length>0){
				
				page = page+(retorno.length);
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

