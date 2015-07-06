$(document).ready(function()
{	
	$("#todasImagenes").bind("click",
		function(){
			if(active != null){
				$("#"+active).removeClass("active");
			}
			else{
				$("#generall").slideDown();
			}
			$(this).addClass("active");
			active = $(this).attr("id");

		}
	);
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
});
