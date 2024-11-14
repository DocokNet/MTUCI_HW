import React, { useState } from "react";
import { View, TextInput, Button, StyleSheet } from "react-native";
import TodoList from "../components/TodoList";

const HomeScreen = () => {
  const [text, setText] = useState("");
  const [todos, setTodos] = useState([]);
  const [editingTodo, setEditingTodo] = useState(null);

  const addTodo = () => {
    if (text.trim()) {
      setTodos([...todos, { id: Date.now(), text, completed: false }]);
      setText("");
    }
  };

  const deleteTodo = (id) => {
    setTodos(todos.filter((todo) => todo.id !== id));
  };

  const editTodo = (id) => {
    const todo = todos.find((todo) => todo.id === id);
    setEditingTodo(todo);
    setText(todo.text);
  };

  const saveEditedTodo = () => {
    if (text.trim()) {
      const updatedTodos = todos.map((todo) => {
        if (todo.id === editingTodo.id) {
          return { ...todo, text };
        }
        return todo;
      });
      setTodos(updatedTodos);
      setEditingTodo(null);
      setText("");
    } else {
      Alert.alert("Ошибка", "Поле задачи не может быть пустым");
    }
  };

  const cancelEditing = () => {
    setEditingTodo(null);
    setText("");
  };

  const toggleComplete = (id) => {
    setTodos(
      todos.map((todo) =>
        todo.id === id ? { ...todo, completed: !todo.completed } : todo
      )
    );
  };

  return (
    <View style={styles.container}>
      <TextInput
        style={styles.input}
        placeholder="Введите задачу"
        value={text}
        onChangeText={setText}
      />
      {editingTodo ? (
        <>
          <Button title="Сохранить" onPress={saveEditedTodo} />
          <Button title="Отмена" onPress={cancelEditing} />
        </>
      ) : (
        <Button title="Добавить" onPress={addTodo} />
      )}
      <TodoList
        todos={todos}
        onDelete={deleteTodo}
        onEdit={editTodo}
        onToggleComplete={toggleComplete}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 40,
  },
  input: {
    padding: 10,
    borderColor: "#ccc",
    borderWidth: 1,
    borderRadius: 5,
    marginBottom: 10,
  },
});

export default HomeScreen;
