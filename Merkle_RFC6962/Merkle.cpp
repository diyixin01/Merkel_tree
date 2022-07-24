#include"Merkle.h"



int main()
{
	Merkle_tree();
	if (MT_proof(4))
		cout << "MT_proof Success!" << endl;
	else cout << "MT_proof Error!" << endl;
	if (MT_not_proof(5.5))
		cout << "MT_not_proof Success!" << endl;
	else cout << "MT_not_proof Error!" << endl;

	return 0;
}