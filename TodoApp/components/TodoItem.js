import React from "react";
import {
  View,
  Text,
  TextInput,
  Button,
  StyleSheet,
  FlatList,
  Alert,
  TouchableOpacity,
} from "react-native";
import { FontAwesome5 } from "@expo/vector-icons";

const TodoItem = ({ item, onDelete, onEdit, onToggleComplete }) => {
  return (
    <View style={styles.todoItem}>
      <Text style={styles.todoText}>{item.text}</Text>
      <View style={styles.buttonContainer}>
        <TouchableOpacity onPress={() => onDelete(item.id)}>
          <FontAwesome5 name="trash" size={20} color="#f00" />
        </TouchableOpacity>
        <TouchableOpacity onPress={() => onEdit(item.id)}>
          <FontAwesome5 name="edit" size={20} color="#007bff" />
        </TouchableOpacity>
        <TouchableOpacity onPress={() => onToggleComplete(item.id)}>
          <FontAwesome5
            name={item.completed ? "check-circle" : "circle"}
            size={20}
            color={item.completed ? "#28a745" : "#ccc"}
          />
        </TouchableOpacity>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  todoItem: {
    padding: 10,
    marginVertical: 5,
    backgroundColor: "#f8f9fa",
    borderRadius: 5,
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
  },
  todoText: {
    fontSize: 16,
  },
  buttonContainer: {
    flexDirection: "row",
    gap: 5,
  },
});

export default TodoItem;
