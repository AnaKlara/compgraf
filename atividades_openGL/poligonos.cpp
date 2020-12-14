#include <windows.h>  
#include <GL/glut.h>  
 

void initGL() {
   glClearColor(0.0f, 0.0f, 0.0f, 1.0f); // preto e opaco
}
 
/* Manipulador para evento de repintura de janela.
Liga de volta quando a janela aparecer pela primeira vez e sempre que a janela precisar ser pintada novamente. */
void display() {
   glClear(GL_COLOR_BUFFER_BIT);   
 

   glBegin(GL_QUADS);              // 4 vértices de um quad
      glColor3f(1.0f, 0.0f, 0.0f); // vermelho
      glVertex2f(-0.8f, 0.1f);     // Defina vértices em ordem anti-horária (CCW)
      glVertex2f(-0.2f, 0.1f);     
      glVertex2f(-0.2f, 0.7f);
      glVertex2f(-0.8f, 0.7f);
 
      glColor3f(0.0f, 1.0f, 0.0f); // verde
      glVertex2f(-0.7f, -0.6f);
      glVertex2f(-0.1f, -0.6f);
      glVertex2f(-0.1f,  0.0f);
      glVertex2f(-0.7f,  0.0f);
 
      glColor3f(0.2f, 0.2f, 0.2f); // cinza escuro
      glVertex2f(-0.9f, -0.7f);
      glColor3f(1.0f, 1.0f, 1.0f); // Branco
      glVertex2f(-0.5f, -0.7f);
      glColor3f(0.2f, 0.2f, 0.2f); // Cinza escuro
      glVertex2f(-0.5f, -0.3f);
      glColor3f(1.0f, 1.0f, 1.0f); // Branco
      glVertex2f(-0.9f, -0.3f);
   glEnd();
 
   glBegin(GL_TRIANGLES);          // 3 vértices de um triângulo
      glColor3f(0.0f, 0.0f, 1.0f); // Azul
      glVertex2f(0.1f, -0.6f);
      glVertex2f(0.7f, -0.6f);
      glVertex2f(0.4f, -0.1f);
 
      glColor3f(1.0f, 0.0f, 0.0f); // vermelho
      glVertex2f(0.3f, -0.4f);
      glColor3f(0.0f, 1.0f, 0.0f); // Verde
      glVertex2f(0.9f, -0.4f);
      glColor3f(0.0f, 0.0f, 1.0f); // Azul
      glVertex2f(0.6f, -0.9f);
   glEnd();
 
   glBegin(GL_POLYGON);            // vértices de um polígono fechado
      glColor3f(1.0f, 1.0f, 0.0f); // Amarelo
      glVertex2f(0.4f, 0.2f);
      glVertex2f(0.6f, 0.2f);
      glVertex2f(0.7f, 0.4f);
      glVertex2f(0.6f, 0.6f);
      glVertex2f(0.4f, 0.6f);
      glVertex2f(0.3f, 0.4f);
   glEnd();
 
   glFlush();  // Renderiza
}
 

int main(int argc, char** argv) {
   glutInit(&argc, argv);          // inicializa GLUT
   glutCreateWindow("poligonos e cores");  // nome da janela
   glutInitWindowSize(320, 320);   // tamanho inicial da janela
   glutInitWindowPosition(50, 50); // posição inicial da janela
   glutDisplayFunc(display);       // evento call back
   initGL();                       // inicializa openGL
   glutMainLoop();                 // loop de ventos
   return 0;
}