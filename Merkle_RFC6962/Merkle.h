#pragma once
#include<iostream>
#include <functional>
#include <string>

using namespace std;
std::hash<std::string> h;

struct MT
{
	int depth = -1;
	int num = -1;
	int left = -1;
	int right = -1;
	int parent = -1;
	string hash_i;
};

const int num = 100000;
int num1 = num;
int num2 = 0;
int tdepth = 0;
int r = 0;
int q = -1;
int p = -1;
MT arr[2 * num];

string Hash(string str)
{
	size_t n = h(str);
	string New_str = to_string(n);
	return New_str;
}

void Change_depth(MT* tmp)
{
	if (tmp->left == -1 && tmp->right == -1)
	{
		tmp->depth++;
		return;
	}
	Change_depth(&(arr[tmp->left]));
	tmp->depth++;
	Change_depth(&(arr[tmp->right]));
}

void Merkle_tree()
{
	int num_1 = 0;
	int i = 0;
	do
	{
		int c = i;
		int d = i - num2;
		for (i; i < num1 + c; i++)
		{
			if (num1 != num)
			{
				if (p != -1)
				{
					arr[i].left = p;
					arr[p].parent = i;
					arr[i].right = d;
					arr[d].parent = i;
				}
				else
				{
					arr[i].left = d;
					arr[d].parent = i;
					arr[i].right = d + 1;
					arr[d + 1].parent = i;
				}

				d = d + 2;
				arr[i].depth = tdepth;
				arr[i].num = arr[arr[i].left].num + arr[arr[i].right].num;
				arr[i].hash_i = Hash(arr[arr[i].left].hash_i + arr[arr[i].right].hash_i);
			}
			else
			{
				arr[i].depth = tdepth;
				arr[i].num = i;
				arr[i].hash_i = Hash(to_string(i));
			}
		}
		if (num1 == 1)
		{
			num_1++;
		}
		if (num_1 == 2)
			return;
		if ((num1 + r) % 2 == 0)
		{
			num2 = num1;
			num1 = (num1 + r) / 2;
			r = 0;
			p = q;
			q = -1;
		}
		else
		{
			if (q == -1)
			{
				q = i - 1;
			}
			Change_depth(&(arr[q]));
			num2 = (num1);
			num1 = (num1 + r) / 2;
			r = 1;
		}
		tdepth++;
	} while (num1 > 0);
}

bool MT_proof(int points)
{
	if (arr[points].left != -1 && arr[points].right != -1)
	{
		return 0;
	}
	string b = Hash(to_string(arr[points].num));
	int c = points;
	do
	{
		int a = arr[c].parent;
		if (arr[a].right != c)
		{
			b = Hash(b + arr[arr[a].right].hash_i);
		}
		else b = Hash(arr[arr[a].left].hash_i + b);
		c = a;
	} while (arr[c].parent != -1);
	if (b == arr[c].hash_i)
		return 1;
	else return 0;
}

bool MT_not_proof(double points)
{
	int a = points;
	int b = a + 1;
	bool b1 = MT_proof(a);
	bool b2 = MT_proof(b);
	if (b1 && b2)
	{
		return 1;
	}
	else return 0;
}