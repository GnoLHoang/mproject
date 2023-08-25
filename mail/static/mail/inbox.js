document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  document.querySelector("#compose-form").addEventListener('submit', email_sender);
  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views 
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#email-detail').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#email-detail').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Show the emails the user have
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(data => {
    console.log(data);
    // Loop through each email
    data.forEach(item => {
      // Create an email container
      const childElement = document.createElement('div');
      childElement.className = 'mailbox-item'
      childElement.innerHTML = `<strong>Sender: ${item.sender}</strong>: ${item.subject}  ||  <i>${item.timestamp}</i>`
      childElement.addEventListener('click', function() {
        document.querySelector('#emails-view').style.display = 'none';
        document.querySelector('#compose-view').style.display = 'none';
        document.querySelector('#email-detail').style.display = 'block';
        console.log(item.id);
        emailDetail(item.id);
      })
      document.querySelector('#emails-view').appendChild(childElement);
      if (item.read === true) {
        childElement.style.backgroundColor = '#c5c9c6';
      }
    })
  })
}

function email_sender(event) {
  event.preventDefault();
  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
      recipients: document.querySelector('#compose-recipients').value,
      subject: document.querySelector('#compose-subject').value,
      body: document.querySelector('#compose-body').value
    })
  })
  .then(response => response.json())
  .then(data => {
    load_mailbox('sent');
  })

}


function emailDetail(id) {
  fetch(`/emails/${id}`)
  .then(response => response.json())
  .then(email => {
    const sender = email.sender;
    const recipient = email.recipients;
    const subject = email.subject;
    const body = email.body;
    const timestamp = email.timestamp;
    const archiveStatus = email.archived === false ? "Archive" : "Unarchive"
    // Header
    
    document.querySelector('#email-detail').innerHTML = `
    <div id="header" style="position: relative">
      <strong>From</strong>: ${sender} <strong>to</strong> ${recipient}
      <br>
      <strong>Subject</strong>: ${subject}
      <br>
      <strong>Timestamp</strong>: ${timestamp}
      <button id="reply-button" type="button" class="btn btn-outline-primary">Reply</button>
      <button id="archive-button" type="button" class="btn btn-outline-danger">${archiveStatus}</button>
    </div>
    <hr>
    <h1>--${subject}--</h1>
    ${body}
    `

    document.querySelector('#reply-button').addEventListener('click', () => {
      const CurEmail = email;

      document.querySelector('#emails-view').style.display = 'none';
      document.querySelector('#compose-view').style.display = 'block';
      document.querySelector('#email-detail').style.display = 'none';
      
      document.querySelector('#compose-recipients').value = `${CurEmail.sender}`;
      // Check if the email subject already starts with "Re:"
      document.querySelector('#compose-subject').value = CurEmail.subject.startsWith("Re:") ? CurEmail.subject : `Re: ${CurEmail.subject}`
      document.querySelector('#compose-body').value = `
      On ${CurEmail.timestamp} ${CurEmail.sender} wrote:
      
      ${CurEmail.body}
      `;
    });
    document.querySelector('#archive-button').addEventListener('click', () => {
      const CurEmail = email;
    
      if (CurEmail.archived === false) {
        fetch(`/emails/${CurEmail.id}`, {
          method: 'PUT',
          body: JSON.stringify({
            archived: true
          })
        })
      } else {
        fetch(`/emails/${CurEmail.id}`, {
          method: 'PUT',
          body: JSON.stringify({
            archived: false
          })
        })
      }
      
      load_mailbox('inbox')
    });

  });

  fetch(`/emails/${id}`, {
    method: 'PUT',
    body: JSON.stringify({
        read: true
    })
  })
}


