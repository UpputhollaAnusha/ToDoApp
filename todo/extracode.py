# {% block content %}

# {% if form.errors %}
# <p>Your username and password didn't match. Please try again.</p>
# {% endif %}

# {% if next %}
#     {% if user.is_authenticated %}
#     <p>Your account doesn't have access to this page. To proceed,
#     please login with an account that has access.</p>
#     {% else %}
#     <p>Please login to see this page.</p>
#     {% endif %}
# {% endif %}

# <form method="post" action="{% url 'todolist' %}">
# {% csrf_token %}
# <table>
# <tr>
#     <td>{{ form.username.label_tag }}</td>
#     <td>{{ form.username }}</td>
# </tr>
# <tr>
#     <td>{{ form.password.label_tag }}</td>
#     <td>{{ form.password }}</td>
# </tr>
# </table>

# <input type="submit" value="Signin">
# <input type="hidden" name="next" value="{{ next }}">
# </form>
# {% endblock %}