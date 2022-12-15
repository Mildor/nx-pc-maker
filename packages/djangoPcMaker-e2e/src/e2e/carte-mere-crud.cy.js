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
  cy.get('a[href*="/pcMaker/motherBoard/"]').click()
})

describe('CRUD MotherBoard', () => {

  it('create', () => {
    cy.get('[data-cy="motherboard_Marque"]').should("be.visible").type("TEST")

    cy.get('[data-cy="motherboard_Chipset"]').should("be.visible").type("0000")

    cy.get('[data-cy="motherboard_submit"]').should("be.visible").click()

    cy.get('table').contains('td', 'TEST').should('be.visible');
    cy.get('table').contains('td', '0000').should('be.visible');
  })

  it('Modify', ()=>{
    const parent = cy.contains("tr","TEST").children();
    parent.find('[data-cy="motherboard_modify"]').click();

    cy.get('[data-cy="motherboard_Marque"]').should("be.visible").clear().type("Tes")

    cy.get('[data-cy="motherboard_Chipset"]').should("be.visible").clear().type("ter")

    cy.get('[data-cy="motherboard_submit"]').should("be.visible").contains("Modifier").click()

    cy.get('table').contains('td', 'Tes').should('be.visible');
    cy.get('table').contains('td', 'ter').should('be.visible');
  })

  it('Delete', ()=>{
    const parent = cy.contains("tr","Tes").children();
    parent.find('[data-cy="motherboard_delete"]').click();

    cy.get('table').contains('td', 'Tes').should('not.exist');
    cy.get('table').contains('td', 'ter').should('not.exist');
  })

})
