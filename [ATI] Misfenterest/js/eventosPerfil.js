$(document).ready(function()
{	
	$("#misGalerias").bind("click",
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
	$("#meGusta").bind("click",
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
	$("#editarPerfil").bind("click",
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
	$("#cerrarModificar").bind("click",
		function(){
			$("#editar").css("display","none");
			$("#barra").removeClass("opacar");
			$("#perfil").removeClass("opacar");
			$("#columnas").removeClass("opacar");
		}
	);
	$("#verMiPerfil").attr("href","perfil.html");
	$("#guardarPerfil").bind("click",
		function(){
			//validar entrada

			$("#editar").addClass("opacar");
			$("#mensajeExito").slideDown();	
		}
	);
	$("#aceptarMensaje").bind("click",
		function(){
			$("#editar").css("display","none");
			$("#editar").removeClass("opacar");
			$("#barra").removeClass("opacar");
			$("#perfil").removeClass("opacar");
			$("#columnas").removeClass("opacar");
			$("#mensajeExito").slideUp();	
		}
	);
});
