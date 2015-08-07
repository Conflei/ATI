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
	$("#editarPerfil").click(
		function(){
			$("#editar").css("display","block");
			$("#barra").addClass("opacar");
			$("#perfil").addClass("opacar");
			$("#columnas").addClass("opacar");
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
	$("#guardarPerfil").click(
		function(){
			//validar entrada
			if($("#nombreUsr").attr("value") != null && $("#nombreUsr").attr("value") != "")
			{
				var name = document.getElementById('nombreUsr').value;
				var lastname = document.getElementById('apellidoUsr').value;
				var usr = document.getElementById('Usr').value;
			    if(name!= null && name != "" && lastname != null && lastname != "" && usr != null && usr != "")
			    {
					$("#editar").addClass("opacar");
					$("#mensajeExito").slideDown();
				}	
			}


		}
	);


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
	$("#cerrar").click(
		function(){
			$("#contenido").slideUp();
			$("#barra").removeClass("opacar");
			$("#perfil").removeClass("opacar");
			$("#columnas").removeClass("opacar");		
		}
	);
});


$(window).scroll(function(){
	if ($(window).scrollTop() == $(document).height() - $(window).height()){
		generationUP();
	}					
});


function mostrarImagen(id){
	$("h4").text(title(id));
	$("#parContent").text(description(id));
	$("#imgContent").attr("src",urlImg(id));
	
	$("#barra").addClass("opacar");
	$("#perfil").addClass("opacar");
	$("#columnas").addClass("opacar");
	
	$("#contenido").slideDown();
}

$("#cargarImagen").change(function(){
	alert("holaaa ");
});

