#include <iostream>
#include <cmath>

using namespace std;

const float LOAD_FACTOR_GROW = 1.0;
const float LOAD_FACTOR_SHRINK = 0.25;
const int INITIAL_CAPACITY = 8;

struct Node {
    int key;
    int value;
    Node* next;
    Node* prev;

    Node(int k, int v) : key(k), value(v), next(nullptr), prev(nullptr) {}
};

struct LinkedList {
    Node* head;
    Node* tail;

    LinkedList() : head(nullptr), tail(nullptr) {}

    void insert(int key, int value) {
        Node* newNode = new Node(key, value);
        if (!head) {
            head = tail = newNode;
        } else {
            tail->next = newNode;
            newNode->prev = tail;
            tail = newNode;
        }
    }

    bool remove(int key) {
        Node* current = head;
        while (current) {
            if (current->key == key) {
                if (current->prev)
                    current->prev->next = current->next;
                else
                    head = current->next;

                if (current->next)
                    current->next->prev = current->prev;
                else
                    tail = current->prev;

                delete current;
                return true;
            }
            current = current->next;
        }
        return false;
    }

    Node* find(int key) {
        Node* current = head;
        while (current) {
            if (current->key == key)
                return current;
            current = current->next;
        }
        return nullptr;
    }

    void clear() {
        Node* current = head;
        while (current) {
            Node* toDelete = current;
            current = current->next;
            delete toDelete;
        }
        head = tail = nullptr;
    }

    ~LinkedList() {
        clear();
    }
};

class HashTable {
private:
    LinkedList* *table;
    int capacity;
    int size;
    float A;

    int hash(int key) {
        float frac = fmod(key * A, 1.0f);
        return static_cast<int>(floor(capacity * frac));
    }

    void resize(int new_capacity) {
        LinkedList** old_table = table;
        int old_capacity = capacity;

        capacity = new_capacity;
        table = new LinkedList*[capacity];
        for (int i = 0; i < capacity; ++i) {
            table[i] = new LinkedList();
        }

        size = 0;
        for (int i = 0; i < old_capacity; ++i) {
            Node* current = old_table[i]->head;
            while (current) {
                insert(current->key, current->value);
                current = current->next;
            }
            delete old_table[i];
        }
        delete[] old_table;
    }

public:
    HashTable() {
        capacity = INITIAL_CAPACITY;
        table = new LinkedList*[capacity];
        for (int i = 0; i < capacity; ++i) {
            table[i] = new LinkedList();
        }
        size = 0;
        A = (sqrt(5.0f) - 1) / 2; // golden ratio fraction
    }

    void insert(int key, int value) {
        if ((float)size / capacity >= LOAD_FACTOR_GROW) {
            resize(capacity * 2);
        }
        int index = hash(key);
        Node* found = table[index]->find(key);
        if (found) {
            found->value = value;
        } else {
            table[index]->insert(key, value);
            ++size;
        }
    }

    bool remove(int key) {
        int index = hash(key);
        bool removed = table[index]->remove(key);
        if (removed) {
            --size;
            if ((float)size / capacity <= LOAD_FACTOR_SHRINK && capacity > INITIAL_CAPACITY) {
                resize(capacity / 2);
            }
        }
        return removed;
    }

    int* get(int key) {
        int index = hash(key);
        Node* node = table[index]->find(key);
        return node ? &node->value : nullptr;
    }

    ~HashTable() {
        for (int i = 0; i < capacity; ++i) {
            delete table[i];
        }
        delete[] table;
    }
};

int main() {
    HashTable ht;
    ht.insert(10, 100);
    ht.insert(18, 200);
    ht.insert(26, 300);

    int* val = ht.get(18);
    if (val) cout << "Value at key 18: " << *val << endl;

    ht.remove(18);
    val = ht.get(18);
    if (!val) cout << "Key 18 not found." << endl;

    return 0;
}
