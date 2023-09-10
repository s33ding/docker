# Use the official Fedora image
FROM fedora:latest

# Install the OpenSSH client
RUN dnf install -y openssh-clients

# Create a directory for SSH keys (optional)
RUN mkdir -p /root/.ssh

# Set a default command (you can override this when running the container)
CMD ["/bin/bash"]
