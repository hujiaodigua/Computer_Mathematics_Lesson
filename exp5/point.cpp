#include"Point.h"
// ������������� 
Point::Point()
{
}
Point::~Point()
{
}
//���û�ͼʱ�ĺ������������  
void Point::setpx(double x)
{ 
     px=x;
}

void Point::setpy(double y)
{
     py=y;
}

//��ȡ��ͼʱ�ĺ������������  

double Point::getpx() const
{ 
       return px;
}
double Point::getpy() const
{
       return py;
}
