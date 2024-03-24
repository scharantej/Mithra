## Design for a Flask Application to Create a Landing Page for a Donation Campaign for Mental Health

### HTML Files

- **landing_page.html**: This is the main landing page for the campaign. It will contain the necessary elements to engage users and encourage them to donate. The page will include:
  - A clear and concise headline describing the purpose of the campaign.
  - A brief explanation of the importance of mental health and the impact of donations.
  - Compelling call-to-action buttons that allow users to donate directly.
  - A contact form to allow users to get in touch with the campaign organizers.
- **success.html**: This page will be displayed to users after they have successfully made a donation. It will include:
  - A thank-you message for their contribution.
  - Information about how their donation will be used to support mental health initiatives.

### Routes

- **index**: This route will render the landing page (`landing_page.html`) when a user visits the root URL of the application.
- **donate**: This route will handle the donation process. It will accept a donation amount from the user and redirect them to the payment gateway.
- **success**: This route will be called after a successful payment and will render the success page (`success.html`).
- **contact**: This route will handle the contact form submission. It will validate the user's input and send an email to the campaign organizers.