const editButtons = document.getElementsByClassName('btn-edit');
const reviewText = document.getElementById('id_content');
const reviewRating = document.getElementById('id_rating');
const reviewForm = document.getElementById('reviewForm');
const submitButton = document.getElementById('submitButton');

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");
/**
 * Initializes edit functionality for the provided edit buttons.
 * 
 * For each button in the `editButtons` collection:
 * - Retrieves the associated review's ID upon click.
 * - Fetches the content of the corresponding review.
 * - Populates the `reviewText ` input/textarea with the review's content for editing.
 * - Populates the `rating`  input with the review's rating for edting.
 * - Updates the submit button's text to "update".
 * - Sets the form's action attribute to the `'edit_review/<review_id>' end point.
 */

for (let button of editButtons){
    button.addEventListener('click', (e)=>{
        let reviewId = e.target.getAttribute('review_id');
        let reviewRatingId = e.target.getAttribute('review_rating_id')
        let reviewContent = document.getElementById(`review${reviewId}`).innerText;
        reviewText.value = reviewContent;
        reviewRating.value = reviewRatingId;
        submitButton.innerText = 'Update';
        reviewForm.setAttribute('action', `edit_review/${reviewId}`); 
    })
}

 /**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated review's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific review.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let reviewId = e.target.getAttribute("review_id");
      deleteConfirm.href = `delete_review/${reviewId}`;
      deleteModal.show();
    });
  }