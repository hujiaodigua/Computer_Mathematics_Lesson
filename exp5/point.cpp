#include"Point.h"
// 构造和析构函数 
Point::Point()
{
}
Point::~Point()
{
}
//设置绘图时的横坐标和纵坐标  
void Point::setpx(double x)
{ 
     px=x;
}

void Point::setpy(double y)
{
     py=y;
}

//获取绘图时的横坐标和纵坐标  

double Point::getpx() const
{ 
       return px;
}
double Point::getpy() const
{
       return py;
}
