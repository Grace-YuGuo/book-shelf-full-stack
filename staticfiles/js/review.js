const editButtons = document.getElementsByClassName('btn-edit');
const reviewText = document.getElementById('id_content');
const reviewRating = document.getElementById('id_rating');
const reviewForm = document.getElementById('reviewForm');
const submitButton = document.getElementById('submitButton');


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