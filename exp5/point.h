#ifndef POINT_H    //������� 
#define POINT_H
  
class Point{
      public:
             Point();
             ~Point();
             
             void setpx(double x);
             void setpy(double y);             
             
             double getpx() const;   //��ȡ��ͼʱ�ĺ����� ��������  
             double getpy() const;    
             
      private:
              
              double px;    // ��ͼʱ�ĺ����� 
              double py;     // ��ͼʱ�������� 
      };
#endif
