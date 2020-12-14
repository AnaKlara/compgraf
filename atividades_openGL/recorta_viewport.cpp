#include <windows.h> 
#include <GL/glut.h> 
 
void initGL() {
   // cor de fundo
   glClearColor(0.0f, 0.0f, 0.0f, 1.0f); // preto e opaco
}
 
void display() {
   glClear(GL_COLOR_BUFFER_BIT);  
 
  
   glBegin(GL_QUADS);             
      glColor3f(1.0f, 0.0f, 0.0f); 
      glVertex2f(-0.8f, 0.1f);    
      glVertex2f(-0.2f, 0.1f);     
      glVertex2f(-0.2f, 0.7f);
      glVertex2f(-0.8f, 0.7f);
 
      glColor3f(0.0f, 1.0f, 0.0f);
      glVertex2f(-0.7f, -0.6f);
      glVertex2f(-0.1f, -0.6f);
      glVertex2f(-0.1f,  0.0f);
      glVertex2f(-0.7f,  0.0f);
 
      glColor3f(0.2f, 0.2f, 0.2f); 
      glVertex2f(-0.9f, -0.7f);
      glColor3f(1.0f, 1.0f, 1.0f); 
      glVertex2f(-0.5f, -0.7f);
      glColor3f(0.2f, 0.2f, 0.2f); 
      glVertex2f(-0.5f, -0.3f);
      glColor3f(1.0f, 1.0f, 1.0f); 
      glVertex2f(-0.9f, -0.3f);
   glEnd();
 
   glBegin(GL_TRIANGLES);          
      glColor3f(0.0f, 0.0f, 1.0f); 
      glVertex2f(0.1f, -0.6f);
      glVertex2f(0.7f, -0.6f);
      glVertex2f(0.4f, -0.1f);
 
      glColor3f(1.0f, 0.0f, 0.0f); 
      glVertex2f(0.3f, -0.4f);
      glColor3f(0.0f, 1.0f, 0.0f); 
      glVertex2f(0.9f, -0.4f);
      glColor3f(0.0f, 0.0f, 1.0f); 
      glVertex2f(0.6f, -0.9f);
   glEnd();
 
   glBegin(GL_POLYGON);            
      glColor3f(1.0f, 1.0f, 0.0f); 
      glVertex2f(0.4f, 0.2f);
      glVertex2f(0.6f, 0.2f);
      glVertex2f(0.7f, 0.4f);
      glVertex2f(0.6f, 0.6f);
      glVertex2f(0.4f, 0.6f);
      glVertex2f(0.3f, 0.4f);
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
   glutCreateWindow("muda tamanho da Viewport");  
   glutDisplayFunc(display);      
   glutReshapeFunc(reshape);       
   initGL();                       
   glutMainLoop();                
   return 0;
}