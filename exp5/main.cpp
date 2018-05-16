#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
#include"Point.h"
using namespace std;
int main()
{
	const int SPEEDLIMITED=70;                
	double speed,maxSpeed,minSpeed,upperSpeed,lowerSpeed;      
	int groupNumber=8,interval;                       
    vector<double> vecSpeed;                    
	vector<double>::iterator temp1,temp2;      
	cout<<"请输入车辆速度,按ctrl+z结束..."<<endl;
	//区间车速原始数据输入
    while(cin>>speed)                         
    {
		if(!(speed>0 && speed<=SPEEDLIMITED))
			cout<<"数据有误，请重新输入!";
		else
            vecSpeed.push_back(speed); 
     }
	//原始数据从小到大进行排序
	sort(vecSpeed.begin (),vecSpeed.end());             
	//找出最大速度、最小速度、组距
	temp1=max_element(vecSpeed.begin (),vecSpeed.end()); 
	maxSpeed=*temp1;                                    
	temp2=min_element(vecSpeed.begin (),vecSpeed.end());
	minSpeed=*temp2;
	interval=(maxSpeed-minSpeed)/(groupNumber-1);
	//计算出绘制速度频率分布曲线时的速度上限和下限
	upperSpeed=(int)maxSpeed+1;                          
	lowerSpeed=(int)minSpeed-1;
	cout<<upperSpeed<<" "<<lowerSpeed<<" "<<interval<<endl;
    
    vector<Point> speedPoint;                           
    Point tempPoint;                                     
    double temp,leftBoundary=minSpeed,rightBoundary=leftBoundary+interval; 
	double midSpeed;                                    
	vector<double>::iterator iter;                       

	//计算速度组中间值(横坐标)及分组车速出现的频率(纵坐标)
   for( int i=0;i!=groupNumber;++i)                       
     {
	      temp=0;                                      
          for(iter=vecSpeed.begin();iter!=vecSpeed.end();++iter)  
		   {
		       if( (*iter>=leftBoundary) && (*iter<rightBoundary) )  
			   {
			     ++temp;
			   }
		   }
          tempPoint.setpy((temp/vecSpeed.size())*100);
          tempPoint.setpx(leftBoundary+interval/2.0);
		  speedPoint.push_back( tempPoint);
		  leftBoundary=rightBoundary;
		  rightBoundary+=interval;
	 }   
   //观察横坐标和纵坐标值
	for( vector<Point>::size_type nt=0; nt!=speedPoint.size() ;++nt)
	{
		cout<<nt<<":x:"<<speedPoint.at(nt).getpx()<<" y:"<<speedPoint.at(nt).getpy()<<endl;
	}   
    //输出为MATLAB支持的.m文件，以便于在MATLAB中进一步分析
    ofstream fout("speed.m");       
	if(!fout)                                                 
	{
		cerr<<" error unable to open output file! "<<endl;
		return -1;
	}
  // 横坐标
	fout<<" x=[ ";             
	for(vector<Point>::iterator itera=speedPoint.begin();itera!=speedPoint.end();++itera)
	{
		fout<<(*itera).getpx()<<"  ";
	}
	fout<<"]"<<endl;
  //纵坐标
	fout<<" y=[ ";          
	for( itera=speedPoint.begin();itera!=speedPoint.end();++itera)
	{
		fout<<(*itera).getpy()<<"  ";
	}
	fout<<"]"<<endl;
	fout<<"plot(x,y)"<<endl;
	fout<<"hold on"<<endl;    
	return 0;  
}
