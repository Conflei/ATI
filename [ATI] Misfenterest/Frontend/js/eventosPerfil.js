$(document).ready(function()
{	
	
	generationUP();
	$("#misGalerias").click(
		function(){
			if(active != null){
				$("#"+active).removeClass("active");
			}
			else{
				$("#general").slideDown();
			} 
			$(this).addClass("active");
			active = $(this).attr("id");

		}
	);
	$("#meGusta").click(
		function(){
			if(active != null){
				$("#"+active).removeClass("active");
			}
			else{
				$("#general").slideDown();
			}
			$(this).addClass("active");
			active = $(this).attr("id");

		}
	);

	$("#cancelarPerfil").bind("click",
		function(){
			$("#editar").css("display","none");
			$("#barra").removeClass("opacar");
			$("#perfil").removeClass("opacar");
			$("#columnas").removeClass("opacar");
		}
	);
	$("#cerrarModificar").click(
		function(){
			$("#editar").css("display","none");
			$("#barra").removeClass("opacar");
			$("#perfil").removeClass("opacar");
			$("#columnas").removeClass("opacar");
		}
	);
	$("#editarPerfil").click(function (){
		//$("#myModalEditarPerfil").modal();
		$("#editar").css("display","block");
		$("#barra").addClass("opacar");
		$("#perfil").addClass("opacar");
		$("#columnas").addClass("opacar");
		
		
	});


	$("#aceptarMensaje").click(
		function(){
			$("#editar").css("display","none");
			$("#editar").removeClass("opacar");
			$("#barra").removeClass("opacar");
			$("#perfil").removeClass("opacar");
			$("#columnas").removeClass("opacar");
			$("#mensajeExito").slideUp();	
		}
	);
	$("#aceptarMensajeError").click(
		function(){
			$("#editar").css("display","none");
			$("#editar").removeClass("opacar");
			$("#barra").removeClass("opacar");
			$("#perfil").removeClass("opacar");
			$("#columnas").removeClass("opacar");
			$("#mensajeError").slideUp();	
		}
	);
	$("#cerrar").click(
		function(){
			$("#contenido").slideUp();
			$("#barra").removeClass("opacar");
			$("#perfil").removeClass("opacar");
			$("#columnas").removeClass("opacar");		
		}
	);

	$("#verMiPerfil").hover(function(){
		$("#botonPerfilOpciones").slideDown()
		$(this).css("background-color", "white");
    }, function(){
		
	});
	$("#verMiPerfil").click(function(){
		$("#botonPerfilOpciones").slideToggle()
	});
	$("body").click(function(){
		$(verMiPerfil).css("background-color", "#D8D8D8");
		$("#botonPerfilOpciones").slideUp()
	});
	$(".tipo").click(function(){
		general = !general;
		generationUP();
	});

	
});


$(window).scroll(function(){
	if ($(window).scrollTop() == $(document).height() - $(window).height()){
		generationUP();
	}					
});


function mostrarImagen(index){
	//alert("holaaaa");
	if(isPin[index])
			$("#opPin").text("Despinear!");
	else
		$("#opPin").text("Pinear!");
	if(general){
		$("h4").text(images[index]["author"]);
		$("#parContent").text(images[index]["description"]);
		$("#imgContent").attr("src",images[index]["picdir"]);
		
		$("#barra").addClass("opacar");
		$("#perfil").addClass("opacar");
		$("#columnas").addClass("opacar");
		
		$("#contenido").slideDown();
	}
	else{
		$("h4").text(imagesPin[index]["author"]);
		$("#parContent").text(imagesPin[index]["description"]);
		$("#imgContent").attr("src",imagesPin[index]["picdir"]);
		
		$("#barra").addClass("opacar");
		$("#perfil").addClass("opacar");
		$("#columnas").addClass("opacar");
		$("#opPin").text("Despinear!");
		$("#contenido").slideDown();
	}
}


function verLobby(name){
		//alert("holaaaa"+name);
		var form = $('<form action="/verLobby" method="post">' +
	
		 '<input type="text" name="Name" value="'+name+'">' +
		   '<button type="submit" id="sub"></button>'+
		  '</form>');
		$('body').append(form);
		$("#sub").click();
}


function guardarPerfil(name){
		//validar entrada
	var respuesta;
	var nameusr = $("#nombreUsr").val();
	var cargarImagen = $("#cargarImagen").val();
	var userAbout = $("#userAbout").val();
	//alert(name+" "+nameusr+" "+userAbout+" "+cargarImagen);
	if(cargarImagen.length>0){ //hay que crear un formulario
		var button = $('<button type="submit" id="subm"></button>');
		$('#formEditarPerfil').attr("action","/editarPerfilForm")
		$('#formEditarPerfil').append(button);
		$("#subm").click();
	}
	else{ //se hace con ajax
		
		respuesta = doAjaxEditarPerfil(name,nameusr,userAbout);
		$("#editar").addClass("opacar");
	}
	
	if(respuesta){
		$("#showFullName").text(nameusr);
		$("#showDescription").text(userAbout);
		$("#mensajeExito").slideDown();
		
	}
	else{
		$("#mensajeError").slideDown();
	}
	var cargarImagen = $("#cargarImagen").val("");

}

function cambiarPassword(name){
	
	$("#myModalEditar").modal();
	
}

function doPin(name){
	var picdir = $('#imgContent').attr("src");
	var namebutton = "Despinear!";
	//alert(name+" Hizo Pin a "+picdir);
	if($("#opPin").text() == "Pinear!"){
		doAjaxPin(name,picdir,"pin");
	}
	else{
		doAjaxPin(name,picdir,"despin");
		namebutton = "Pinear!";
	}
	$('#cerrar').click();	
	$('#opPin').text(namebutton);
}


