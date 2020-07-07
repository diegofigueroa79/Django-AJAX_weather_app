$(document).readyfunction(function(){

    // ajax function for adding city
    $('#formButton').click(function(){
        let serialData = $('#form').serialize();
        let addUrl = $(this).data('url');
        $.ajax({
            'url': addUrl,
            'data': serialData,
            'type': 'post',
            'success': function(response) {
                $('#taskList').add(
                    `<ul class="list-group">
						<div class="media">
							<img src="http://openweathermap.org/img/w/{{ city.icon }}.png" alt="" class="mr-3">
							<div class="media-body">
								<h5 class="mt-0">
									{{ city.name }}, {{ city.country }}
								</h5>
								<p>
									{{ city.temp }}<span>&#176;</span>F</li>
								</p>
								<p>
									{{ city.description|title }}
								</p>
							</div>
						</div>
						<a href="{% url 'weather:delete' city.name %}" class="close" role="button">
							<span aria-hidden="true">&times;</span>
						</a>
					</ul>`
                );
            }
        });
    });

});