describe('Logging In - CSRF Tokens', function () {
  const username = 'admin'
  const password = 'admin'

  Cypress.Commands.add('loginByCSRF', (csrfToken) => {
    cy.request({
      method: 'POST',
      url: 'http://127.0.0.1:8000/pcMaker/login/',
      failOnStatusCode: false, // dont fail so we can make assertions
      form: true, // we are submitting a regular form body
      body: {
        username,
        password,
        _csrf: csrfToken, // insert this as part of form body
      },
    })
  })

  /**
   * Check that we are in the Home page
   */
  const inHomePage = () => {
    cy.location('href').should('match', /http:\/\/127\.0\.0\.1:8000\/pcMaker\//i)
  }

  it('go to login page', () => {
    cy.visit('http://127.0.0.1:8000/pcMaker/login/')
    cy.location('href').should('match', /http:\/\/127\.0\.0\.1:8000\/pcMaker\/login\//i)
  })

  it('Login with bad CSRF', function () {
    // first show that by not providing a valid CSRF token
    // that we will get a 403 status code
    cy.loginByCSRF('invalid-token')
      .its('status')
      .should('eq', 403)
  })

  it('Login', () => {
    cy.visit('http://127.0.0.1:8000/pcMaker/login/')
    cy.get('input[name=username]').type(username)
    cy.get('input[name=password]').type(password)
    cy.get('form').submit()
    inHomePage()
  })
})
