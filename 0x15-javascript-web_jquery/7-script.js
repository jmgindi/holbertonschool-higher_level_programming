$(function () {
  $.get('http://swapi.co/api/people/5/?format=json', function (data) {
    $('div#character').text(data.name);
  });
});
