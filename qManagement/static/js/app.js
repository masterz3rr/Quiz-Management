$('#startQuiz').on('show.bs.modal', function (event) {

  var button = $(event.relatedTarget); // Button that triggered the modal
  var quizId = button.data('value'); // Extract the data-value

  // Update the href of the modal link
  var modalLink = $(this).find('.quizLink');
  console.log("click")
  modalLink.attr('href', "{% url 'studentExam' " + quizId + " %}");
});
