#include <iostream>
#include <stdexcept>

class DynamicArray {
private:
    int* data;
    int capacity;
    int length;

    void resize(int new_capacity) {
        int* new_data = new int[new_capacity];
        for (int i = 0; i < length; ++i)
            new_data[i] = data[i];
        delete[] data;
        data = new_data;
        capacity = new_capacity;
    }

public:
    DynamicArray() : capacity(4), length(0) {
        data = new int[capacity];
    }

    ~DynamicArray() {
        delete[] data;
    }

    void push_back(int value) {
        if (length == capacity)
            resize(capacity * 2);
        data[length++] = value;
    }

    void pop_back() {
        if (length > 0)
            --length;
    }

    int get(int index) const {
        if (index < 0 || index >= length)
            throw std::out_of_range("Index out of bounds");
        return data[index];
    }

    void set(int index, int value) {
        if (index < 0 || index >= length)
            throw std::out_of_range("Index out of bounds");
        data[index] = value;
    }

    int size() const {
        return length;
    }

    int get_capacity() const {
        return capacity;
    }
};
int main() {
    DynamicArray arr;
    arr.push_back(10);
    arr.push_back(20);
    arr.push_back(30);
    arr.push_back(40);
    arr.push_back(50); // triggers resize

    for (int i = 0; i < arr.size(); ++i)
        std::cout << arr.get(i) << " ";
    std::cout << "\n";

    arr.pop_back();
    std::cout << "Size after pop: " << arr.size() << "\n";

    return 0;
}
