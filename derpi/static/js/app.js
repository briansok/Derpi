// Main App Scripts

function saveNotification() {
	UIkit.notification('Your changes are saved', {status:'success'});
}

function errorNotification() {
	UIkit.notification('Something went wrong', {status:'failed'});
}

$(function() {
	var selectedClass = "";
	$(".filter").click(function(){ 
		selectedClass = $(this).attr("data-group"); 
		$(".sensor-overview").fadeTo(100, 0.1);
		$(".sensor-overview .sensor-item").not("."+selectedClass).fadeOut();
		setTimeout(function() {
			$("."+selectedClass).fadeIn();
			$(".sensor-overview").fadeTo(300, 1);
			}, 300); 

	});

	 var clockElement = document.getElementById( "clock" );

	 function updateClock ( clock ) {
		 if (clockElement) {
			 clock.innerHTML = new Date().toLocaleTimeString();
		 }
	 }

	 setInterval(function () {
		 updateClock( clockElement );
	 }, 1000);


	$('#widget-choice').on('change', function(){
		if ($(this).val() == "sensor") {
			$(".form-item").not(".sensor-list, .widget-list").hide();
			$('.sensor-list').fadeIn();
			 console.log('werkt');
		}	

		if ($(this).val() == "controller") {
			$(".form-item").not(".controller-list, .widget-list").hide();
			$('.controller-list').fadeIn();
		}	

		if ($(this).val() != "sensor" && $(this).val() != "controller") {
			$('.sensor-list').hide();
			$('.controller-list').hide();
		}	
	}); 
	$('#widget-choice').trigger('change');

});

