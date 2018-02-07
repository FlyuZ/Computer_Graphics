#include <gl/glut.h>
#include <math.h>
#include <time.h>
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

const float AngleToRadion = 3.14159 / 180.0;

class Objmodel {
private:
	//objģ����Ϣ
	vector<vector<GLfloat>> vertex;
	vector<vector<GLfloat>> vertex_texture;
	vector<vector<GLfloat>> vertex_normal;
	vector<vector<int>> face_vertex;
	vector<vector<int>> face_texture;
	vector<vector<int>> face_normal;
	GLint v_num;
	GLint vt_num;
	GLint vn_num;
	GLint f_num;

	//����obj�߽�㣬����ģ�Ͱ�Χ��
	vector<GLfloat> center;
	vector<GLfloat> one0fcatercorner;		    //��Χ�жԽ�����һ����
	vector<GLfloat> other0fcatercorner;		    //��Χ�жԽ�������һ����
public:
	Objmodel();
	~Objmodel();

	//���ļ��ж�ȡ����
	void readFile(string path);

	//��ʾģ������
	void showObj(GLint mode1, GLint mode2);

	//����obj��Χ������	��������ƽ�Ƶ�ԭ��
	vector<GLfloat> getCenter();

	//����ģ�Ͷ��㷨��
	void calculateNormal();

	//����ģ�͵İ�Χ��
	void drawBox();
};