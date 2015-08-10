var body;
var mainContainer;
var grid;
var gridSizer;
var $isoGrid;
var firstFill = false;
var showingIMG = false;

$(document).ready(function(){
	$("#myBtn").click(function(){
		$("#myModal").modal();
	});
	ini();
	$('#cerrar').bind('click', function(){
		hideSeleccion();
	});
	//	fill();

});

$(window).scroll(function(){
	if($(window).scrollTop() + $(window).height() == getDocHeight())
	{
		//alert("holaa "+page);
		//fill();
	}
})


function getDocHeight()
{
	var D = document;
	return Math.max(
			D.body.scrollHeight, D.documentElement.scrollHeight,
			D.body.offsetHeight, D.documentElement.offsetHeight,
			D.body.clientHeight, D.documentElement.clientHeight
		);
}



var isoOptions = {
	itemSelector: '.grid-item',
  	percentPosition: true,
  	layoutMode: 'masonry',
  	masonry:{
  		columnWidth:'.grid-sizer',
  		gutter:23
  	  }
}

function ini(){

	body = $(".allContent");

	mainContainer = $("<div>");
	mainContainer.attr("class", "mainContent");
	
	grid = $("<div>");
	grid.attr("class", "grid");

	gridSizer =  $("<div>");
	gridSizer.attr("class", "grid-sizer");

	grid.append(gridSizer);
	mainContainer.append(grid);

	body.prepend(mainContainer);
	$isoGrid = $('.grid').isotope(isoOptions);

	firstFill = true;
	showingIMG = false;
}


function UploadContent(){
	$("#myModal").modal();
}

function hideSeleccion(){
		$('.contenidoSelecto').slideUp('slow');
		$('.allContent').attr("onclick", "showImage()");
		$('.allContent').css("opacity", "1");
	
	
};

function fill()
{
		var username = $("#nombreUsuario").text();
		//alert(username);
		//var Objetos = doAjaxPage("all",username);
		var Objetos = "fallo";
		//alert(Objetos);
		if(Objetos && Objetos != "fallo"){
			for(i = 0; i<Objetos.length; i++)
			{
				//alert(Objetos[i]["picdir"] + " "+ Objetos[i]["title"] + " "+ Objetos[i]["description"] + " "+ Objetos[i]["author"] + " "+ Objetos[i]["isPin"]);
				if(Objetos[i]["isPin"]=="True"){
					isPin[cant] = true;
				}
				else{
					isPin[cant] = false;
				}
				var gridElement = $("<div>");
				var rand = (Math.floor(Math.random()*10) % 2)+1;
				
				//if(rand==0) gridElement.attr("class", "grid-item grid-item--height3");
				if(rand==1) gridElement.attr("class", "grid-item grid-item--height2");
				if(rand==2) gridElement.attr("class", "grid-item");
				//if(rand==3) gridElement.attr("class", "grid-item grid-item--height1");

				var elemento = $("<div>");
				elemento.attr("class", "miElemento");

				var imagen = $("<img>");
				imagen.attr("src",Objetos[i]["picdir"]);
				imagen.attr("onclick", "showImage("+cant+")");
				elemento.append(imagen);
				elemento.append("<hr>");
				elemento.append("<p>"+Objetos[i]["title"]);
				elemento.append("<p>"+Objetos[i]["description"]);
				elemento.append("<hr>");

				var imagenPerfil = $("<img>");
				imagenPerfil.attr("src", "img/misael.jpg"); //OJO ESTE DATO ESTA CABLEADO -> aqui va la foto de quien subio la imagen
				imagenPerfil.attr("id", "profile");

				elemento.append(imagenPerfil);

				var link = $("<a>")
				link.attr("href", "#;");
				link.attr("class", "userName");
				link.attr("id", "profileName");
				link.append(Objetos[i]["author"]);
				elemento.append(link);

				gridElement.append(elemento);
				$isoGrid.append(gridElement).isotope('appended', gridElement);
				cant = cant + 1; //cantidad de imagenes			
			}
			misObjetos = misObjetos.concat(Objetos);
		}
		
		
}

function verMiPerfil(name){
		//alert("holaaaa"+name);
		var form = $('<form action="/myprofile" method="post">' +
	
		 '<input type="text" name="name" value="'+name+'">' +
		   '<button type="submit" id="sub"></button>'+
		  '</form>');
		$('body').append(form);
		$("#sub").click();
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

function showImage(index)
{
			if(isPin[index])
				$("#opPin").text("Despinear!");
			else
				$("#opPin").text("Pinear!");
			$('.contenidoSelecto').slideDown('fast');
			$('.allContent').css("opacity", "0.4");
			$('h4').text(misObjetos[index]["author"]);
			$('#parContent').text(misObjetos[index]["description"]);
			$('#imgContent').attr("src", misObjetos[index]["picdir"]);
			
			showingIMG = true;
};



