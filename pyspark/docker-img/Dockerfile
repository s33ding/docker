# Set environment variables
FROM bitnami/spark:3.5.4-debian-12-r2

# Switch to root to install system packages
USER root

# Install Vim, curl, unzip, and wget (useful for debugging)
RUN install_packages vim curl unzip wget

# Set correct environment variables (SPARK_CONF_DIR should be a directory)
ENV HADOOP_CONF_DIR=/opt/bitnami/hadoop/etc/hadoop/
ENV SPARK_CONF_DIR=/opt/bitnami/spark/conf
ENV SPARK_HOME=/opt/bitnami/spark
ENV PYSPARK_PYTHON=python3
ENV PATH=$SPARK_HOME/bin:$PATH

# Install AWS CLI
RUN curl -sSL "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install \
    && rm -rf awscliv2.zip aws

# Copy Python requirements file and install dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Download MySQL Connector JAR and place it in Spark's jars directory
RUN curl -L "https://repo1.maven.org/maven2/com/mysql/mysql-connector-j/8.3.0/mysql-connector-j-8.3.0.jar" \
    -o /opt/bitnami/spark/jars/mysql-connector-j-8.3.0.jar

# Ensure correct permissions
RUN chown 1001:1001 /opt/bitnami/spark/jars/mysql-connector-j-8.3.0.jar

# Ensure the necessary directories exist
RUN mkdir -p /opt/bitnami/spark/conf/
RUN mkdir -p /opt/bitnami/hadoop/etc/hadoop/

# Ensure correct ownership for non-root users
RUN chown -R 1001:1001 /opt/bitnami/spark/conf/
RUN chown -R 1001:1001 /opt/bitnami/hadoop/etc/hadoop/

COPY core-site.xml /opt/bitnami/hadoop/etc/hadoop/core-site.xml


RUN chmod 644 /opt/bitnami/hadoop/etc/hadoop/core-site.xml

# Copy the entrypoint script and ensure execution permissions
COPY entrypoint.sh /opt/bitnami/spark/entrypoint.sh
RUN chmod +x /opt/bitnami/spark/entrypoint.sh

# Switch back to non-root user
USER 1001
