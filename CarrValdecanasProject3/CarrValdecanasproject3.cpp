/*
Name: Michael Carr & Nicky Valdecanas
Project 3 Trie and TST
Due Date: 11/22/2019
 */

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <ctime>
#include <ctype.h>
#include <bits/stdc++.h>
#include <sstream>
#include <iterator>
#include <algorithm>


using namespace std;

vector<string>autoList;
vector<string>TSTList;
//used to get all the nodes for space complexity of the trie
long long int total = 0;
//used to get all the nodes for space complexity of the TST
long long int TSTnode = 0;


//----------------------------Trie-----------------------------------
// Alphabet size (# of symbols) 
#define ALPHABET_SIZE (26) 
  
// Converts key current character into index 
// use only 'a' through 'z' and lower case 
#define CHAR_TO_INDEX(c) ((int)c - (int)'a') 
  
// trie node 
struct TrieNode 
{ 
    struct TrieNode *children[ALPHABET_SIZE]; 
  
    // isWordEnd is true if the node represents 
    // end of a word 
    bool isWordEnd; 
}; 
  
// Returns new trie node (initialized to NULLs) 
struct TrieNode *getNode(void) 
{ 
    struct TrieNode *pNode = new TrieNode; 
    pNode->isWordEnd = false; 
  
    for (int i = 0; i < ALPHABET_SIZE; i++) 
        pNode->children[i] = NULL; 

    total++;
    return pNode; 
} 
  
// If not present, inserts key into trie.  If the 
// key is prefix of trie node, just marks leaf node 
void insert(struct TrieNode *root,  const string key) 
{ 
    struct TrieNode *pCrawl = root; 
  
    for (int level = 0; level < key.length(); level++) 
    { 
        int index = CHAR_TO_INDEX(key[level]); 
        if (!pCrawl->children[index]) {
	  total++;
	  pCrawl->children[index] = getNode();
	}
	total++;
        pCrawl = pCrawl->children[index]; 
    } 
    total++;
    // mark last node as leaf 
    pCrawl->isWordEnd = true; 
} 
  
// Returns true if key presents in trie, else false 
bool search(struct TrieNode *root, const string key) 
{ 
    int length = key.length(); 
    struct TrieNode *pCrawl = root; 
    for (int level = 0; level < length; level++) 
    { 
        int index = CHAR_TO_INDEX(key[level]); 
  
        if (!pCrawl->children[index]) 
            return false; 
  
        pCrawl = pCrawl->children[index]; 
    } 
  
    return (pCrawl != NULL && pCrawl->isWordEnd); 
} 
  
// Returns 0 if current node has a child 
// If all children are NULL, return 1. 
bool isLastNode(struct TrieNode* root) 
{ 
    for (int i = 0; i < ALPHABET_SIZE; i++) 
        if (root->children[i]) 
            return 0; 
    return 1; 
} 
  
// Recursive function to print auto-suggestions for given 
// node. 
void suggestionsRec(struct TrieNode* root, string currPrefix) 
{ 
    // found a string in Trie with the given prefix 
    if (root->isWordEnd) 
    { 
            autoList.push_back(currPrefix); 
    } 
  
    // All children struct node pointers are NULL 
    if (isLastNode(root)) 
        return; 
  
    for (int i = 0; i < ALPHABET_SIZE; i++) 
    { 
        if (root->children[i]) 
        { 
            // append current character to currPrefix string 
            currPrefix.push_back(97 + i);
	     
            // recur over the rest 
            suggestionsRec(root->children[i], currPrefix);
	    currPrefix.pop_back();
        } 
    } 
} 
  
// print suggestions for given query prefix. 
int printAutoSuggestions(TrieNode* root, const string query) 
{ 
    struct TrieNode* pCrawl = root;
     
    // Check if prefix is present and find the 
    // the node (of last level) with last character 
    // of given string. 
    
    int n = query.length();
    //cout << "query length is: " << n << endl;
    for (int level = 0; level < n; level++) 
    { 
        int index = CHAR_TO_INDEX(query[level]); 
  
        // no string in the Trie has this prefix 
        if (!pCrawl->children[index]) 
            return 0; 
  
        pCrawl = pCrawl->children[index];

    } 
  
    // If prefix is present as a word. 
    bool isWord = (pCrawl->isWordEnd == true); 
  
    // If prefix is last node of tree (has no 
    // children) 
    bool isLast = isLastNode(pCrawl); 
  
    // If prefix is present as a word, but 
    // there is no subtree below the last 
    // matching node. 
    if (isWord && isLast) 
    { 
        cout << query << endl; 
        return -1; 
    } 
  
    // If there are are nodes below last 
    // matching character. 
    if (!isLast) 
    { 
        string prefix = query; 
        suggestionsRec(pCrawl, prefix); 
        return 1; 
    } 
} 
  
  
//-------------------------End Trie--------------------------------

//-------------------------Start TST-------------------------------


struct TST {
    char c;
    TST *left;
    TST *mid;
    TST *right;
    bool isEnd;
};
/*
Inserts word by each character. Say word comes in as hello followed by high:
       h
       |
       e
       |\
       l i
       | |
       l g
       | |
       o h
Thats how they will be inserted into a TST.
 */

TST * TSTinsert (TST * head, const char * word) {

  //if a new word
  if (head == NULL) {

    if (word && *word) {
      head = new TST();
      head->c = *word;
      TSTnode++;
      head->mid = TSTinsert(head->mid, ++word);
      if (head->mid == NULL) {
        head->isEnd = true;
      }
    }
  }
  //If first fills mid then depending on letter alphabetical value it's
  //inserted to the left is less than and right if more than.
  else if (*word == head->c) {
     head->mid = TSTinsert(head->mid, ++word);
  }


  else if (*word < head->c) {
     head->left = TSTinsert(head->left, word);
  }

  else
    head->right = TSTinsert(head->right, word);
  return head;
}


/*
This function makes the string. Say for instance the auto complete is for 's'
and the choices are 'swallow' and 'sid'. It will use 's' and tranverse any
's' word letter by letter until it hits a false isEnd variable.
 */


void strungOut(TST * head, const char * prefix) {
  //this keeps the string in tacked as recurrsion is done.
  static string s;
  //if head doesn't equal NULL keep going.
  if (head != NULL) {
    strungOut(head->left, prefix);
    //concatanting the string to be found
    s += head->c;
    if (head->isEnd) {
      cout << ((prefix) ? prefix : (char*)("") ) <<  s << ", ";
      //TSTList.push_back(s);
    }
    strungOut(head->mid, prefix);

    s.pop_back();
    strungOut(head->right, prefix);
  }
}


/*
Get the node to start from with prefix passed. This will then be used to
traverse the string to be searched for.
 */

TST * getHeadForPrefix (TST * head, const char * prefix, TST *& temp) {
    if (prefix && *prefix) {
      if (*prefix < head->c) {
            head->left = getHeadForPrefix(head->left, prefix, temp);
        }
      else if (*prefix > head->c) {
            head->right = getHeadForPrefix(head->right, prefix, temp);
        }

      else {
            if (*(prefix+1) == '\0') {
                temp = head;
            }
 head->mid = getHeadForPrefix(head->mid, ++prefix, temp);
        }
    }
    return head;
}


TST * strungOutWithPrefix(TST * head, const char * prefix) {
    TST * temp = new TST();
    getHeadForPrefix(head, prefix, temp);
    if (temp != NULL) {
      strungOut(temp->mid, prefix);

    }

    return temp;
}

bool searchTST(TST *head, char* pattern)
{
 while (head != NULL)
 {
  if (*pattern < head->c)
   head = head->left;
  else if (*pattern == head->c)
  {
   //If end of string flag is found and the pattern length is also exhausted, 
   //we can safely say that the pattern is present in the TST
    if (head->isEnd && *(pattern + 1) == '\0')
    return true;
   pattern++;
   head = head->mid;
  }
  else
   head = head->right;
 }

 return false;
}


//---------------------------End of TST----------------------------

int main(int argc, char*argv[])
{
  // For flags
  int flag = atoi(argv[2]);

    
  //variables and data bucket to be used
  ifstream input; string filename; string word; char c; vector<string>words;
  long long int n = 0;

  //User inputs file name and opens it
  //cout<<"Enter the file name: ";
  filename = argv[1];
  input.open(filename.c_str());

  while (input.get(c)){
    //if a character is a letter and if check whether its upper or lowercase, concatenate
    //it with other letters
    if (isalpha(c)){
      if(isupper(c)){
	c = tolower(c);
	word += c;
      }
      else{
	word += c;
      }
    }
    //if character is a given symbol, do nothing
    //probably not needed
    else if (c == ',' || c == '.' || c == ':' || c == ';' || c == '?'){
    }

    //if a character is a space or end of line
    //make word equal empty string
    else if (c == ' ' || c == '\n'){

      words.push_back(word);
      n++;
      word = "";
    }

  }

  //n is word count making an array of strings of size n
  //convert vector to array
  /*string keys[n];
  for (long long int i = 0; i < words.size(); i++) {
    keys[i] = words.at(i);
    }
  */
  //words.clear();
  //prints array for debugging
  /*for(int i = 0; i < n; i++){
  cout << keys[i] << endl;
  }*/

  struct TrieNode *root = getNode();

  // Construct trie
  clock_t start, end;
  //calculating time(start)
  start = clock();
  for (long long int i = 0; i < words.size(); i++) {
    //cout << keys[i] << endl;
    insert(root, words.at(i));
  }
  //(end)
  end = clock();
    
  double trieTime = ((double) (end - start)) / CLOCKS_PER_SEC;
  
  //Construct a TST

  TST * head = NULL;
  start = clock();
  for (long long int i = 0; i < words.size(); i++) {
    string word = words.at(i);
    const char *charword = word.c_str();
      head = TSTinsert(head, (char*)(charword));

  }
  //(end)
  end = clock();
    
  double TSTTime = ((double) (end - start)) / CLOCKS_PER_SEC;
  
  
  cout << "Time taken to build the standard Trie is " << flush;
  cout << trieTime << flush;
  cout << " and space occupied by it is " << flush;
  cout << total << endl;
  
  cout << "Time taken to build the BST based Trie is " << flush;
  cout << TSTTime << flush;
  cout << " and space occupied by it is " << flush;
  cout << TSTnode << endl << endl;
  
  //Find all occurance with a user specified prefix
  if(flag == 1){
    
    string userString;
    //bool used to stop the do while, if using only "0" it will seg fault
    bool ans = true;
    do{
      cout << "Enter search string(enter 0 to exit): ";
      cin >> userString;
      if (userString == "0")
	ans = false;

      else{

	//--------------------------Trie------------------------------
	//Standard search for the string
	clock_t start, end;
	start = clock();
	search(root, userString);
	//end time for standard search
	end = clock();
	double searchTime = ((double) (end - start)) / CLOCKS_PER_SEC;
	cout << "Time taken to search in the standard Trie is " << flush;
	cout << searchTime << endl;
	//start time auto complete
	start = clock();
	int comp = printAutoSuggestions(root, userString);
	//end time to auto complete
	end = clock();
	double autoTime = ((double) (end - start)) / CLOCKS_PER_SEC;

	if(comp == -1)
	  cout << "No other strings found with prefix" << endl;

	else if(comp == 0)
	  cout << "No strings found with this prefix" << endl;

	else if(comp == 1){
	  //printing the words found with commas
	  cout << "Auto-complete results using standard Trie are: " << flush;
	  for (auto iter = autoList.begin(); iter != autoList.end(); iter++) {
	    if (iter != autoList.begin()) cout << ", ";
	    cout << *iter;
	  }
	}
	//clearing the list for the next search
	autoList.clear();
	cout << endl;
	//printing the time taken
	cout << "Time taken to find auto-complete results in the standard Trie is " << flush;
	cout << autoTime << endl << endl;
	

      //---------------------------TST-----------------------------------
	//str is need to pass into the search function
	char *str = new char[userString.length()+1];
	strcpy(str, userString.c_str());
	bool success = false;

	//search
	start = clock();
	success = searchTST(head, str);
	end = clock();
	double TSTSearch = ((double) (end - start)) / CLOCKS_PER_SEC;

	cout << "Time taken to search in the BST based Trie is " << TSTSearch << endl;
       
	//auto complete
	cout << "Auto-complete results using BST based Trie is: " << flush;
	start = clock();
	
	strungOutWithPrefix(head, userString.c_str());
        
	end = clock();
	double TSTAuto = ((double) (end - start)) / CLOCKS_PER_SEC;
	cout << '\b' << '\b';
	cout << " ";
	cout << endl;

	//Time taken to auto-complete
	cout << "Time taken to find auto-complete results in the BST based Trie is " << TSTAuto << endl << endl;
	//------------------------------------------------------------------
	
      }
    }while(ans == true);
    
  }
  else{ //flag == 2
    //To search all the keys, no reason to change
    //Trie
    clock_t searchStart, searchEnd;
    searchStart = clock();
    for(long long int i = 0; i < word.size(); i++)
      search(root,words.at(i));
    searchEnd = clock();
    double searchTime = ((double) (searchEnd - searchStart)) / CLOCKS_PER_SEC;
    cout << "Time taken to search all the strings in the standard Trie is ";
    cout << searchTime << endl;

    //TST
    searchTime = 0;
    searchStart = clock();
    for(long long int i = 0; i < words.size(); i++){
      bool success;
      string userString = words.at(i);
      char *str = new char[userString.length()+1];
      strcpy(str, userString.c_str());
      success = searchTST(head, str);
    }
    searchEnd = clock();
    searchTime = ((double) (searchEnd - searchStart)) / CLOCKS_PER_SEC;
    cout << "Time taken to search all the strings in the BST based Trie ";
    cout << searchTime << endl;
  }
  return 0;

}
