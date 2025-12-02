describe('Bookmark Functionality', () => {
  beforeEach(() => {
    cy.visit('http://localhost:5173/login');

    // Spy on the network request
    cy.intercept('POST', '**/login').as('loginRequest');

    // Enter Credentials
    cy.get('input[name="email"]').type('abthevillain@gmail.com');
    cy.get('input[name="password"]').type('1234567890');
    cy.get('button[type="submit"]').click();

    // Wait for login to complete
    cy.wait('@loginRequest', { timeout: 30000 });
    
    // Verify we are on the home page
    cy.url({ timeout: 10000 }).should('eq', 'http://localhost:5173/');
  });

  it('should allow a user to bookmark a job', () => {
    // 1. Wait for the "Loading jobs..." text to DISAPPEAR
    // This ensures the API has finished and React has rendered the real list
    cy.contains('Loading jobs...', { timeout: 20000 }).should('not.exist');

    // 2. Now it is safe to look for the job cards
    cy.get('[data-testid^="job-card-"]', { timeout: 10000 })
      .should('have.length.gt', 0) // Ensure at least one job exists
      .first()
      .within(() => {
        // Click the bookmark button
        cy.get('[data-testid="bookmark-btn"]').click();
      });
  });
});