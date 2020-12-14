#include <windows.h>  
#include <GL/glut.h>  
 
/* inicializa OpenGl  */
void initGL() {
   // cor de fundo
   glClearColor(0.0f, 0.0f, 0.0f, 1.0f); // preto e opaco
}
 
/* Manipulador para evento de repintura de janela. Ligue de volta quando a janela aparecer pela primeira vez e
    sempre que a janela precisar ser pintada novamente. */
void display() {
   glClear(GL_COLOR_BUFFER_BIT);    // Limpa o buffer de cor
   glMatrixMode(GL_MODELVIEW);      
   glLoadIdentity();                
 
   glTranslatef(-0.5f, 0.4f, 0.0f); // Translata para a esquerda e para cima
   glBegin(GL_QUADS);               // Cada conjunto de 4 vértices forma um quad
      glColor3f(1.0f, 0.0f, 0.0f);  // vermelho
      glVertex2f(-0.3f, -0.3f);     // Define vértices em ordem anti-horária 
      glVertex2f( 0.3f, -0.3f);    
      glVertex2f( 0.3f,  0.3f);
      glVertex2f(-0.3f,  0.3f);
   glEnd();
 
   glTranslatef(0.1f, -0.7f, 0.0f); // direita e para baixo
   glBegin(GL_QUADS);               // Cada conjunto de 4 vértices forma um quad
      glColor3f(0.0f, 1.0f, 0.0f); // verde
      glVertex2f(-0.3f, -0.3f);
      glVertex2f( 0.3f, -0.3f);
      glVertex2f( 0.3f,  0.3f);
      glVertex2f(-0.3f,  0.3f);
   glEnd();
 
   glTranslatef(-0.3f, -0.2f, 0.0f); 
   glBegin(GL_QUADS);               
      glColor3f(0.2f, 0.2f, 0.2f); 
      glVertex2f(-0.2f, -0.2f);
      glColor3f(1.0f, 1.0f, 1.0f); 
      glVertex2f( 0.2f, -0.2f);
      glColor3f(0.2f, 0.2f, 0.2f); 
      glVertex2f( 0.2f,  0.2f);
      glColor3f(1.0f, 1.0f, 1.0f); 
      glVertex2f(-0.2f,  0.2f);
   glEnd();
 
   glTranslatef(1.1f, 0.2f, 0.0f); // 
   glBegin(GL_TRIANGLES);          // triangulos
      glColor3f(0.0f, 0.0f, 1.0f); // azul
      glVertex2f(-0.3f, -0.2f);
      glVertex2f( 0.3f, -0.2f);
      glVertex2f( 0.0f,  0.3f);
   glEnd();
 
   glTranslatef(0.2f, -0.3f, 0.0f);    
   glRotatef(180.0f, 0.0f, 0.0f, 1.0f); 
      glBegin(GL_TRIANGLES);               
      glColor3f(1.0f, 0.0f, 0.0f); 
      glVertex2f(-0.3f, -0.2f);
      glColor3f(0.0f, 1.0f, 0.0f); 
      glVertex2f( 0.3f, -0.2f);
      glColor3f(0.0f, 0.0f, 1.0f); 
      glVertex2f( 0.0f,  0.3f);
   glEnd();
 
   glRotatef(-180.0f, 0.0f, 0.0f, 1.0f); 
   glTranslatef(-0.1f, 1.0f, 0.0f);    
   glBegin(GL_POLYGON);                
      glColor3f(1.0f, 1.0f, 0.0f); 
      glVertex2f(-0.1f, -0.2f);
      glVertex2f( 0.1f, -0.2f);
      glVertex2f( 0.2f,  0.0f);
      glVertex2f( 0.1f,  0.2f);
      glVertex2f(-0.1f,  0.2f);
      glVertex2f(-0.2f,  0.0f);
   glEnd();
 
   glFlush();   
}
 

void reshape(GLsizei width, GLsizei height) {  
   
   if (height == 0) height = 1;          
   GLfloat aspect = (GLfloat)width / (GLfloat)height;
 

   glViewport(0, 0, width, height);
 
 
   glMatrixMode(GL_PROJECTION);  
   glLoadIdentity();
   if (width >= height) {

      gluOrtho2D(-1.0 * aspect, 1.0 * aspect, -1.0, 1.0);
   } else {
 
     gluOrtho2D(-1.0, 1.0, -1.0 / aspect, 1.0 / aspect);
   }
}
 

int main(int argc, char** argv) {
   glutInit(&argc, argv);        
   glutInitWindowSize(640, 480);  
   glutInitWindowPosition(50, 50);
   glutCreateWindow("transformacoes"); 
   glutDisplayFunc(display);       
   glutReshapeFunc(reshape);      
   initGL();                       
   glutMainLoop();                 
   return 0;
}