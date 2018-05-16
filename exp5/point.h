#ifndef POINT_H    //定义点类 
#define POINT_H
  
class Point{
      public:
             Point();
             ~Point();
             
             void setpx(double x);
             void setpy(double y);             
             
             double getpx() const;   //获取绘图时的横坐标 和纵坐标  
             double getpy() const;    
             
      private:
              
              double px;    // 绘图时的横坐标 
              double py;     // 绘图时的纵坐标 
      };
#endif
