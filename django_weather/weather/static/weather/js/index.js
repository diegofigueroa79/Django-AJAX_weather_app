$(document).ready(function(){

	let csrfToken = $('input[name=csrfmiddlewaretoken]').val();

    // ajax function for adding city
    $('#formButton').click(function(){
        let serialData = $('#form').serialize();
		let addUrl = $(this).data('url');
        $.ajax({
            'url': addUrl,
            'data': serialData,
            'type': 'post',
            'success': function(response) {
                $('#taskList').append(
                    `<ul class="list-group" data-name="${response['city']['name']}">
						<div class="media">
							<img src="http://openweathermap.org/img/w/${response['city']['icon']}.png" alt="" class="mr-3">
							<div class="media-body">
								<h5 class="mt-0">
									${response['city']['name']}, ${response['city']['country']}
								</h5>
								<p>
									${response['city']['temp']}<span>&#176;</span>F</li>
								</p>
								<p>
									${response['city']['description']}
								</p>
							</div>
						</div>
						<a class="close deleteButton" role="button">
							<span aria-hidden="true">&times;</span>
						</a>
					</ul>`
                );
            }
		});
		$('#form')[0].reset();
	});
	
	$('#taskList').on('click', '.deleteButton', function(){
		let deletebtn = $(this)
		let listGroup = $(deletebtn).parents('.list-group')
		// add custom data-name attribute to .list-group element
		let cityName = listGroup.data('name')
		$.ajax({
			'url': `/delete/${cityName}/`,
			'data': {
				'csrfmiddlewaretoken': csrfToken,
				'name': cityName,
			},
			'type': 'post',
			'success': function(response){
				listGroup.remove();
			}
		})
	})

});