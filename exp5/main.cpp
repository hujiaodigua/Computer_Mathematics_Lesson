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
	cout<<"�����복���ٶ�,��ctrl+z����..."<<endl;
	//���䳵��ԭʼ��������
    while(cin>>speed)                         
    {
		if(!(speed>0 && speed<=SPEEDLIMITED))
			cout<<"������������������!";
		else
            vecSpeed.push_back(speed); 
     }
	//ԭʼ���ݴ�С�����������
	sort(vecSpeed.begin (),vecSpeed.end());             
	//�ҳ�����ٶȡ���С�ٶȡ����
	temp1=max_element(vecSpeed.begin (),vecSpeed.end()); 
	maxSpeed=*temp1;                                    
	temp2=min_element(vecSpeed.begin (),vecSpeed.end());
	minSpeed=*temp2;
	interval=(maxSpeed-minSpeed)/(groupNumber-1);
	//����������ٶ�Ƶ�ʷֲ�����ʱ���ٶ����޺�����
	upperSpeed=(int)maxSpeed+1;                          
	lowerSpeed=(int)minSpeed-1;
	cout<<upperSpeed<<" "<<lowerSpeed<<" "<<interval<<endl;
    
    vector<Point> speedPoint;                           
    Point tempPoint;                                     
    double temp,leftBoundary=minSpeed,rightBoundary=leftBoundary+interval; 
	double midSpeed;                                    
	vector<double>::iterator iter;                       

	//�����ٶ����м�ֵ(������)�����鳵�ٳ��ֵ�Ƶ��(������)
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
   //�۲�������������ֵ
	for( vector<Point>::size_type nt=0; nt!=speedPoint.size() ;++nt)
	{
		cout<<nt<<":x:"<<speedPoint.at(nt).getpx()<<" y:"<<speedPoint.at(nt).getpy()<<endl;
	}   
    //���ΪMATLAB֧�ֵ�.m�ļ����Ա�����MATLAB�н�һ������
    ofstream fout("speed.m");       
	if(!fout)                                                 
	{
		cerr<<" error unable to open output file! "<<endl;
		return -1;
	}
  // ������
	fout<<" x=[ ";             
	for(vector<Point>::iterator itera=speedPoint.begin();itera!=speedPoint.end();++itera)
	{
		fout<<(*itera).getpx()<<"  ";
	}
	fout<<"]"<<endl;
  //������
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
