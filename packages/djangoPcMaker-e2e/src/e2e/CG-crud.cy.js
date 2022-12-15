Cypress.Commands.add("login", ()=>{
  const username = 'admin'
  const password = 'admin'
  cy.visit('http://127.0.0.1:8000/pcMaker/login/')
  cy.get('input[name=username]').type(username)
  cy.get('input[name=password]').type(password)
  cy.get('form').submit()
})

beforeEach(() => {
  cy.login()
  cy.location('href').should('match', /http:\/\/127\.0\.0\.1:8000\/pcMaker\//i)
  cy.get('a[href*="/pcMaker/gpu/"]').click()
})

describe('CRUD CG', () => {

  it('create', () => {
    cy.get('[data-cy="gpu_Marque"]').should("be.visible").type("TEST")

    cy.get('[data-cy="gpu_Modele"]').should("be.visible").type("CG")

    cy.get('[data-cy="gpu_submit"]').should("be.visible").click()

    cy.get('table').contains('td', 'TEST').should('be.visible');
    cy.get('table').contains('td', 'CG').should('be.visible');
  })

  it('Modify', ()=>{
    // eslint-disable-next-line cypress/no-assigning-return-values
    const parent = cy.contains("tr","TEST").children();
    parent.find('[data-cy="gpu_modify"]').click();

    cy.get('[data-cy="gpu_Marque"]').should("be.visible").clear().type("Ceci")

    cy.get('[data-cy="gpu_Modele"]').should("be.visible").clear().type("est")

    cy.get('[data-cy="gpu_submit"]').should("be.visible").contains("Modifier").click()

    cy.get('table').contains('td', 'Ceci').should('be.visible');
    cy.get('table').contains('td', 'est').should('be.visible');
  })

  it('Delete', ()=>{
    const parent = cy.contains("tr","Ceci").children();
    parent.find('[data-cy="gpu_delete"]').click();

    cy.get('table').contains('td', 'Ceci').should('not.exist');
    cy.get('table').contains('td', 'est').should('not.exist');
  })

})
