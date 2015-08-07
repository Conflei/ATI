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
	fill();

});

$(window).scroll(function(){
	if($(window).scrollTop() + $(window).height() == getDocHeight())
	{
		//alert("holaa "+page);
		fill();
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

function showImage(index)
{
			$('.contenidoSelecto').slideDown('fast');
			$('.allContent').css("opacity", "0.4");
			$('#imgContent').attr("src", misObjetos[index]["picdir"]);
			$('h4').html(misObjetos[index]["author"]);
			$('#parContent').html(misObjetos[index]["description"]);
			showingIMG = true;
};

function hideSeleccion(){
		$('.contenidoSelecto').slideUp('slow');
		$('.allContent').attr("onclick", "showImage()");
		$('.allContent').css("opacity", "1");
	
	
};

function fill()
{
		misObjetos = doAjaxPage("all");
		//alert(misObjetos);
		if(misObjetos && misObjetos != "fallo"){
			for(i = 0; i<misObjetos.length; i++)
			{
				//alert(misObjetos[i]["picdir"] + misObjetos[i]["title"] + misObjetos[i]["description"] + misObjetos[i]["author"]);
				var gridElement = $("<div>");
				var rand = Math.floor(Math.random()*10) % 3;
				if(rand==0) gridElement.attr("class", "grid-item grid-item--height3");
				if(rand==1) gridElement.attr("class", "grid-item grid-item--height2");
				if(rand==2) gridElement.attr("class", "grid-item");
				if(rand==3) gridElement.attr("class", "grid-item grid-item--height1");

				var elemento = $("<div>");
				elemento.attr("class", "miElemento");

				var imagen = $("<img>");
				imagen.attr("src",misObjetos[i]["picdir"]);
				imagen.attr("onclick", "showImage("+i+")");
				elemento.append(imagen);
				elemento.append("<hr>");
				elemento.append("<p>"+misObjetos[i]["title"]);
				elemento.append("<p>"+misObjetos[i]["description"]);
				elemento.append("<hr>");

				var imagenPerfil = $("<img>");
				imagenPerfil.attr("src", "img/misael.jpg"); //OJO ESTE DATO ESTA CABLEADO -> aqui va la foto de quien subio la imagen
				imagenPerfil.attr("id", "profile");

				elemento.append(imagenPerfil);

				var link = $("<a>")
				link.attr("href", "#;");
				link.attr("class", "userName");
				link.attr("id", "profileName");
				link.append(misObjetos[i]["author"]);
				elemento.append(link);

				gridElement.append(elemento);
				$isoGrid.append(gridElement).isotope('appended', gridElement);			
			}
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






