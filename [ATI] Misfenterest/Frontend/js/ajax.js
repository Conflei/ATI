function doAjaxPage(){
	var retorno;
	$.ajax({
		type: "GET",
		url: urlImagesLobby,
		data: {'page':page},
		async: false,
		success: function(data){
			retorno = JSON.parse(data);
			//alert("hola soy ajax "+retorno);
			if(retorno != "vacio"){
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
