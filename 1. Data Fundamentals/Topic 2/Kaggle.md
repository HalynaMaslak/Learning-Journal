# IBM HR Analytics Employee Attrition & Performance

**Usability Score**: 8.82
The data set has credibility issues (provenance, timeliness).
Missing coverage refers to gaps or incomplete representations within a dataset, leading to biased or skewed results as the analysis may not capture the full picture.
Missing provenance, on the other hand, means a lack of information about the data's origin, sources, and transformations, making it difficult to assess the trustworthiness and accuracy of the data, as well as trace back and address any potential issues or errors.

## Description
Archive containing all the contents of the IBM HR Analytics Employee Attrition & Performance dataset.

## MD5
MD5 is a cryptographic hash function algorithm that takes the message as input of any length and changes it into a fixed-length message of 16 bytes. MD5 algorithm stands for the **Message-Digest** algorithm. MD5 was developed in 1991 by Ronald Rivest as an improvement of MD4, with advanced security purposes. The output of MD5 (Digest size) is always 128 bits. MD5 is still the most commonly used message digest for non-cryptographic functions, such as used as a checksum to verify data integrity, compressing large files into smaller ones securely, etc.

### Applications of MD5 Algorithm
- MD5 is used as a checksum to verify the integrity of files and data by comparing the hash of the original file with the file received to check if the files or data has been altered.
- MD5 is used for data security and encryption e.g. secure password of users in database and non-sensitive data.
- It is used in version control systems to manage different versions of files.
- It was earlier used in digital signatures and certificate but due to its vulnerabilities, it has been replaced by more secure algorithms like SHA-256.

### Advantages of MD5 Algorithm
- MD5 is faster and simple to understand.
- MD5 algorithm generates a strong password in 16 bytes format. All developers like web developers, etc. use the MD5 algorithm to secure the password of users. 
- To integrate the MD5 algorithm, relatively low memory is necessary. 
- It is very easy and faster to generate a digest message of the original message.

### Disadvantages of MD5 Algorithm
- MD5 generates the same hash function for different inputs (hash collision). 
- MD5 provides poor security over SHA1, SHA256 and other modern cryptographic algorithms.
- MD5 has been considered an insecure algorithm. So now we are using SHA256 instead of MD5. 
- MD5 is neither a symmetric nor asymmetric algorithm.

## QAs:
- Why does using compression aid sustainability and net-zero goals? - It reduces energy consumption (small file are easier to store), which results in lower carbon emissions; it optimises data storage (fewer physical resources are needed); it results in decreased network bandwidth usage and extended hardware span.
- What is the possible issue in identifying the meaning of the column named 'YearsSinceLastPromotion', especially when interpreting the value of '0' in one of the fields? - There is not enough information about the meaning of this value. Has the employee just been promoted? Did they have only one role in the company so this criterion is not applicable?
- Compare the contents of the column 'Over18' and 'OverTime', what data quality issue can you identify? - The column 'Over18' contains 'Y' values while 'OverTime' contains 'Yes' or 'No'. This inconsistency can lead to confusion and human errors while analysing the results.
- What are some possible issues with the data quality of 'MonthlyIncome' and 'Monthly Rate'? - It is not clear what the two fields mean and how they differ.
- How would you validate the 'EmployeeNumber' column and what needs paying special attention to? - This column contains numbers from 1 to 2068, which means the employee number is not standartised and can contain between one and four digits. It makes it more difficult to validate. Even though the numbers seem to be consecutive, some of them are missing.